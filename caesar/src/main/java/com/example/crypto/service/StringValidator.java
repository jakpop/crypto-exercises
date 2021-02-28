package com.example.crypto.service;

import java.util.function.Function;

import static com.example.crypto.service.StringValidator.StringValidationResult.*;

public interface StringValidator extends Function<String, StringValidator.StringValidationResult> {
    static StringValidator isLowerCase() {
        return s -> s.codePoints()
                .mapToObj(c -> (char)c)
                .allMatch(Character::isLowerCase) ? SUCCESS : LOWER_CASE;
    }

    static StringValidator isAlphabet() {
        return s -> s.codePoints()
                .mapToObj(c -> (char)c)
                .allMatch(c -> c >= 97 && c <= 122) ? SUCCESS : CHARS;
    }

    default StringValidator and(StringValidator other) {
        return s -> {
            StringValidationResult result = this.apply(s);
            return result.equals(SUCCESS) ? other.apply(s) : result;
        };
    }

    enum StringValidationResult {
        SUCCESS("Success"),
        LOWER_CASE("String is not all lower case"),
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
