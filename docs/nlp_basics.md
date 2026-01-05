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

### Quick Comparison Table

| Tool | Approach | Result | Speed |
| :--- | :--- | :--- | :--- |
| **Stemming** | Chopping rules | "studi" | 🚀 Blazing Fast |
| **Lemmatization** | Dictionary lookup | "study" | 🐢 Slower |
