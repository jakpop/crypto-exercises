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

}