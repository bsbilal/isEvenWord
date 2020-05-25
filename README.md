# isEvenWord

Problem One: Even Words An even word is a word that contains an even number of copies of every letter. For example, the word“tattletale” is an even word, since there are four copies of 't' and two copies of 'a,' 'e,' and 'l.' Similarly,“appeases” and “arraigning” are even words. However, “banana” is not an even word, because there is just one 'b' and three copies of 'a.'
### isEvenWord(string oldWord)

that accepts as input a string representing a single word and returns whether or not that word is an evenword. Your solution should be recursive and must not use any loops (e.g. while, for). As a hint, thisproblem has a beautiful recursive decomposition:
#### The empty string is an even word, since it has 0 copies of every letter.
#### Otherwise, a word is an even word if there are at least two copies of the first letter and the wordformed by removing two copies of the first letter is itself an even word.For example, we can see that the word “appeases” is an even word using the following logic:

### "appeases"is an even word,because
- "ppeses"is an even word,because
- "eses"is an even word,because
- "ss"is an even word,because
- ""is an even word.

### We also know that “tattletale” is even via the following reasoning:
- "tattletale"is an even word,because
- "atletale"is an even word,because
- "tletle"is an even word,because
- "lele"is an even word,because
- "ee"is an even word,because
- ""is an even word.

Question Source : https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1126/handouts/110%20Assignment%203.pdf
