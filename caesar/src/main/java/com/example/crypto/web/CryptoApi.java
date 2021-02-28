package com.example.crypto.web;

import com.example.crypto.service.CryptoService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/crypto", produces = "application/json")
@RequiredArgsConstructor
public class CryptoApi {

    private final CryptoService cryptoService;

    @RequestMapping(value = "/caesar/cipher")
    public String caesarCipher(@RequestParam(value = "message") String message,
                               @RequestParam(value = "offset") int offset) {
        return cryptoService.caesarCipher(message, offset);
    }

    @RequestMapping(value = "/caesar/decipher")
    public String caesarDecipher(@RequestParam(value = "message") String message,
                                 @RequestParam(value = "offset") int offset) {
        return cryptoService.caesarDecipher(message, offset);
    }
}
