# plover_japanese_kana

A way to write Japanese kana in steno. This is not focused on speed; instead it is meant to be easy to learn for English steno users while still being reasonably efficient. It uses the standard English layout. It works like this:

* Write kana phonetically (`SEN SAI` = せんせい, `MAT TAIR` = まっている, `KAFPL BI KPI` = かーびぃ).
    * The left hand and the vowels generally make one kana -- with those, you can write everything. With the vowels, you can make long vowels like おう and えい as well.
    * Palatized sounds (hya, kya, etc.) can be made by adding `R-`. The rya series is written with `WR-`.
    * Special characters: `KP` + vowel for small kana, vowel + `-FPL` for ー, `KPTU` for っ.
    * To reduce the number of strokes, the right hand can make kana as well, mostly corresponding to common endings (for example, `-R` for る).

## Why?

This plugin is way too slow for any real-time work. In fact, there are other people developing plugins for Plover that would be real-time. However, these require a totally different steno layout.

I made this because I was annoyed that while doing my Japanese vocabulary reviews (which sometimes ask for reading, and sometimes for meaning) I had to switch between steno (for meaning) and Qwerty (for reading) all the time. Now I can do both in steno, and without having to learn a new layout.

## Ideas for future expansion

* Kanji conversion.
    * By default, no kanji conversion would be performed. To trigger conversion, use `*` for the second, third, ... stroke of a word. Then the first IME suggestion will be chosen. Use numbers (`#2`, `#3`, ...) to pick other suggestions. For one-stroke words that you want converted, don't use `*` and just press a number -- but generally it should not be necessary to do that, because you can write a particle or something after it (with `*`).

