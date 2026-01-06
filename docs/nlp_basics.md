# NLP Basics: A Simple Guide

This guide explains the basic concepts of text preprocessing in Natural Language Processing (NLP) using simple words and examples.

---

## 1. Stopwords
**What are they?**  
Stopwords are common words that don't add much meaning to a sentence. Words like "the", "is", "at", "which", and "on" are usually removed to focus on the important keywords.

**Example:**
- **Original:** "The quick brown fox is jumping over the lazy dog."
- **After removing stopwords:** "quick brown fox jumping lazy dog."

---

## 2. Stemming
**What is it?**  
Stemming is a fast, rule-based process that "chops off" the ends of words to find their root form (the "stem"). It doesn't use a dictionary, so it can sometimes create words that aren't real.

### Porter Stemmer vs. Snowball Stemmer

| Feature | Porter Stemmer | Snowball Stemmer |
| :--- | :--- | :--- |
| **History** | Created in 1980; the "grandfather" of stemmers. | A more modern, improved version (Porter2). |
| **Accuracy** | Good, but can be aggressive or weird. | **Better**. It handles edge cases more reliably. |
| **Speed** | Very Fast. | **Slightly Faster** and more efficient. |
| **Language Support** | **English Only**. It is hardcoded for English. | **Multi-lingual**. Supports Spanish, French, German, etc. |

> [!NOTE]
> **Why do we pass "english" to Snowball?**  
> Unlike the Porter Stemmer (which was built *only* for English), the Snowball Stemmer is a multi-language engine. Because it knows the rules for many different languages, you have to tell it which one to use when you initialize it (e.g., `SnowballStemmer("english")` or `SnowballStemmer("spanish")`).
| **Quality** | "history" $\rightarrow$ "histori" | "history" $\rightarrow$ "histori" (Still not a real word). |

**Concept Example:**
- "running", "runs", "ran" $\rightarrow$ **"run"** (Porter/Snowball)
- "finally", "finalized" $\rightarrow$ **"final"** (Snowball is slightly better at these rules)

---

## 3. Lemmatization
**What is it?**  
Lemmatization is a "smart" way to find the root form of a word. Unlike stemming, it uses a dictionary (like WordNet) to make sure the result is a **real word**.

**The Catch:** To work perfectly, it needs to know the **Part of Speech (POS)** (if the word is a noun, verb, or adjective).

**Example:**
- **Stemming:** "eating" $\rightarrow$ "eat" (Simple rule)
- **Lemmatization (Noun):** "eating" $\rightarrow$ "eating" (Defaults to noun)
- **Lemmatization (Verb):** "eating" $\rightarrow$ "eat" (Correctly identifies the action)

---

## Summary: Which one should I use?

1. **Use Stopwords Removal** when you want to reduce noise and focus on important words.
2. **Use Stemming** (specifically Snowball) when you have a massive amount of data and need **speed** over perfect accuracy.
3. **Use Lemmatization** when you need **high accuracy** and real dictionary words (like for chatbots or translation).

---

| **Lemmatization** | Dictionary lookup | "study" | 🐢 Slower |

---

## 4. Part-of-Speech (POS) Tagging
**What is it?**  
POS tagging is the process of labeling each word in a sentence with its grammatical role, like **Noun**, **Verb**, or **Adjective**. It helps the computer understand how words relate to each other.

**Why is it useful?**
- It's essential for **Lemmatization** (to know if a word is a noun or a verb).
- It helps in understanding the context (e.g., "book" can be a noun or a verb).

**Common POS Tags (NLTK):**
- **Noun Tags:**
    - **NN**: Noun, singular (e.g., "dog")
    - **NNS**: Noun, plural (e.g., "dogs")
    - **NNP**: Proper noun, singular (e.g., "India", "John")
    - **NNPS**: Proper noun, plural (e.g., "Americans")
- **Verb Tags:**
    - **VB**: Verb, base form (e.g., "eat")
    - **VBD**: Verb, past tense (e.g., "ate")
    - **VBG**: Verb, gerund or present participle (e.g., "eating")
    - **VBN**: Verb, past participle (e.g., "eaten")
    - **VBP**: Verb, present-tense, non-3rd person (e.g., "eat")
    - **VBZ**: Verb, present-tense, 3rd person (e.g., "eats")
- **Adjective & Adverb Tags:**
    - **JJ**: Adjective (e.g., "big")
    - **JJR**: Adjective, comparative (e.g., "bigger")
    - **JJS**: Adjective, superlative (e.g., "biggest")
    - **RB**: Adverb (e.g., "quickly")
- **Others:**
    - **PRP**: Pronoun (e.g., "I", "you")
    - **DT**: Determiner (e.g., "the", "a")
    - **IN**: Preposition or subordinating conjunction (e.g., "in", "of")
    - **CD**: Cardinal number (e.g., "one", "3000")

**The Rule:** In NLTK, you must **tokenize** your text into a list of words before applying `pos_tag()`.

