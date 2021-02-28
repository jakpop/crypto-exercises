package com.example.crypto.service;

import java.util.function.IntFunction;

import static com.example.crypto.service.OffsetValidator.OffsetValidationResult.NEGATIVE;
import static com.example.crypto.service.OffsetValidator.OffsetValidationResult.SUCCESS;

public interface OffsetValidator extends IntFunction<OffsetValidator.OffsetValidationResult> {

    static OffsetValidator isPositive() {
        return value -> value >= 0 ? SUCCESS : NEGATIVE;
    }

    enum OffsetValidationResult {
        SUCCESS("Success"),
        NEGATIVE("Offset is negative");

        private final String message;

        public String getMessage() {
            return message;
        }

        OffsetValidationResult(final String message) {
            this.message = message;
        }
    }

}
