package com.example.crypto.service;

import com.example.crypto.service.StringValidator.StringValidationResult;
import com.example.crypto.service.OffsetValidator.OffsetValidationResult;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

import static com.example.crypto.service.OffsetValidator.isPositive;
import static com.example.crypto.service.StringValidator.isLowerCaseAlphabet;

@Service
public class CryptoService {

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

        for (int i = 1; i <= 26; i++) {
            results.add(caesarDecipher(message, i));
        }

        return results;
    }

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
