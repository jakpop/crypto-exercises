package com.example.crypto.service;

import com.example.crypto.service.StringValidator.StringValidationResult;
import com.example.crypto.service.OffsetValidator.OffsetValidationResult;
import org.springframework.stereotype.Service;

import static com.example.crypto.service.OffsetValidator.isPositive;
import static com.example.crypto.service.StringValidator.isLowerCaseAlphabet;

@Service
public class CryptoService {

    public String caesarCipher(String message, int offset) {
        validate(message, offset);

        StringBuilder cipherResult = new StringBuilder();
        for (char character : message.toCharArray()) {
            int originalAlphabetPosition = character - 'a';
            int newAlphabetPosition = (originalAlphabetPosition + offset) % 26;
            char newCharacter = (char) ('a' + newAlphabetPosition);
            cipherResult.append(newCharacter);
        }
        return cipherResult.toString();
    }

    public String caesarDecipher(String message, int offset) {
        validate(message, offset);

        return caesarCipher(message, 26 - (offset % 26));
    }

    private void validate(String message, int offset) {
        OffsetValidator.OffsetValidationResult offsetValidationResult = isPositive()
                .apply(offset);

        StringValidationResult stringValidationResult = isLowerCaseAlphabet()
                .apply(message);

        if (stringValidationResult != StringValidationResult.SUCCESS) {
            throw new IllegalArgumentException(stringValidationResult.getMessage());
        }
        if (offsetValidationResult != OffsetValidationResult.SUCCESS) {
            throw new IllegalArgumentException(offsetValidationResult.getMessage());
        }
    }
}
