package com.example.cipher;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class MyCipher {
    public static final char[] normalChar = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };

    public static final char[] codedChar = { 'Q', 'A', 'Z', 'W', 'S', 'X', 'E', 'D', 'C',
            'R', 'F', 'V', 'T', 'G', 'B', 'Y', 'H', 'N',
            'U', 'J', 'M', 'I', 'K', 'O', 'L', 'P' };

    public static String stringEncryption(String s)
    {
        StringBuilder encryptedString = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < 26; j++) {

                if (s.charAt(i) == normalChar[j])
                {
                    encryptedString.append(codedChar[j]);
                    break;
                }

                if (s.charAt(i) < 'a' || s.charAt(i) > 'z')
                {
                    encryptedString.append(s.charAt(i));
                    break;
                }
            }
        }

        return encryptedString.toString();
    }
}

