package com.example.crypto.service;

import com.example.crypto.service.StringValidator.StringValidationResult;
import com.example.crypto.service.OffsetValidator.OffsetValidationResult;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.math3.stat.inference.ChiSquareTest;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

import static com.example.crypto.service.OffsetValidator.isPositive;
import static com.example.crypto.service.StringValidator.isLowerCaseAlphabet;

@Service
@Slf4j
public class CryptoService {

    //algorytmy podebrane z baeldunga :)

    public String caesarCipher(String message, int offset) {
        validate(message, offset);

        StringBuilder cipherResult = new StringBuilder();
        for (char character : message.toCharArray()) {
            if (character != ' ') {
                int originalAlphabetPosition = character - 'a';
                int newAlphabetPosition = (originalAlphabetPosition + offset) % 26;
                char newCharacter = (char) ('a' + newAlphabetPosition);
                cipherResult.append(newCharacter);
            } else {
                cipherResult.append(character);
            }
        }
        return cipherResult.toString();
    }

    public String caesarDecipher(String message, int offset) {
        validate(message, offset);

        return caesarCipher(message, 26 - (offset % 26));
    }

    public List<String> caesarManualBreak(String message) {
        validate(message);

        ArrayList<String> results = new ArrayList<>();

        for (int i = 1; i <= 25; i++) {
            results.add(caesarDecipher(message, i));
        }

        return results;
    }

    /*
    Caesar auto break
     */
    public String caesarAutoBreak(String message) {
        validate(message);

        double[] chiSquares = calculateChiSquares(message);

        int probableOffset = 0;
        for (int offset = 0; offset < chiSquares.length; offset++) {
            log.info(String.format("Chi-Square for offset %d: %.2f", offset, chiSquares[offset]));
            if (chiSquares[offset] < chiSquares[probableOffset]) {
                probableOffset = offset;
            }
        }

        return caesarDecipher(message, probableOffset);
    }

    private double[] calculateChiSquares(String message) {
        //english letters in a text probabilities
        double[] englishLettersProbabilities = {0.073, 0.009, 0.030, 0.044, 0.130, 0.028, 0.016, 0.035, 0.074,
                0.002, 0.003, 0.035, 0.025, 0.078, 0.074, 0.027, 0.003,
                0.077, 0.063, 0.093, 0.027, 0.013, 0.016, 0.005, 0.019, 0.001};

        double[] expectedLettersFrequencies = Arrays.stream(englishLettersProbabilities)
                .map(probability -> probability * message.length())
                .toArray();

        //calculating chi squares
        double[] chiSquares = new double[26];

        for (int offset = 0; offset < chiSquares.length; offset++) {
            String decipheredMessage = caesarDecipher(message, offset);
            long[] lettersFrequencies = observedLettersFrequencies(decipheredMessage);
            double chiSquare = new ChiSquareTest().chiSquare(expectedLettersFrequencies, lettersFrequencies);
            chiSquares[offset] = chiSquare;
        }

        return chiSquares;
    }

    private long[] observedLettersFrequencies(String message) {
        return IntStream.rangeClosed('a', 'z')
                .mapToLong(letter -> countLetter((char) letter, message))
                .toArray();
    }

    private long countLetter(char letter, String message) {
        return message.chars()
                .filter(character -> character == letter)
                .count();
    }

    /*
    VALIDATION
     */
    private void validate(String message, int offset) {
        validate(message);
        validate(offset);
    }

    private void validate(String message) {
        StringValidationResult stringValidationResult = isLowerCaseAlphabet()
                .apply(message);

        if (stringValidationResult != StringValidationResult.SUCCESS) {
            throw new IllegalArgumentException(stringValidationResult.getMessage());
        }
    }

    private void validate(int offset) {
        OffsetValidator.OffsetValidationResult offsetValidationResult = isPositive()
                .apply(offset);

        if (offsetValidationResult != OffsetValidationResult.SUCCESS) {
            throw new IllegalArgumentException(offsetValidationResult.getMessage());
        }
    }
}
