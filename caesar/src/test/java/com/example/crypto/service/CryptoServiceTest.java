package com.example.crypto.service;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(MockitoExtension.class)
class CryptoServiceTest {

    @InjectMocks
    CryptoService cryptoService;

    @Test
    void caesarCipherTest() {
        //given
        String message = "alamakota";
        int offset = 13;

        //when
        String result = cryptoService.caesarCipher(message, offset);

        //then
        assertEquals("nynznxbgn", result);
    }

    @Test
    void caesarDecipherTest() {
        //given
        String message = "nynznxbgn";
        int offset = 13;

        //when
        String result = cryptoService.caesarDecipher(message, offset);

        //then
        assertEquals("alamakota", result);
    }

    @Test
    void validationOfStringTest() {
        //given
        String message = "ALAmaKOTA";
        int offset = 13;

        //when
        IllegalArgumentException result = assertThrows(IllegalArgumentException.class,
                () -> cryptoService.caesarCipher(message, offset));

        //then
        assertEquals("String contains not supported characters", result.getMessage());
    }

    @Test
    void validationNegativeOffsetTest() {
        //given
        String message = "alamakota";
        int offset = -13;

        //when
        IllegalArgumentException result = assertThrows(IllegalArgumentException.class,
                () -> cryptoService.caesarCipher(message, offset));

        //then
        assertEquals("Offset is negative", result.getMessage());
    }

}