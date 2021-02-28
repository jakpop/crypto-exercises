package com.example.crypto.service;

import java.util.function.Function;

import static com.example.crypto.service.StringValidator.StringValidationResult.*;

public interface StringValidator extends Function<String, StringValidator.StringValidationResult> {
    static StringValidator isLowerCaseAlphabet() {
        return s -> s.codePoints()
                .mapToObj(c -> (char)c)
                .allMatch(c -> c >= 97 && c <= 122) ? SUCCESS : CHARS;
    }

    enum StringValidationResult {
        SUCCESS("Success"),
        CHARS("String contains not supported characters");

        private final String message;

        public String getMessage() {
            return message;
        }

        StringValidationResult(final String message) {
            this.message = message;
        }
    }
}
