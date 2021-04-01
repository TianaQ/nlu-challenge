# Linguistics Challenge  

### Task 1: extending the English grammar
 
[JSGF text file](https://github.com/TianaQ/nlu-challenge/blob/master/JSGF_en_ext.txt), [test script in Python](https://github.com/TianaQ/nlu-challenge/blob/master/test.py)  

##### Examples covered by the extended grammar:  

> can you play beatles   
> can you put on paranoid android   
> i want to listen to jazz music    
> play me ummagumma by pink floyd   
> we'd like to hear let it be   
> put on some rock   
> could you play some classic please   

The topic of speech recognition approaches is pretty new to me so my understanding of the matter is limited, but I think that the following issues may occur when adding new entities to the grammar:  
1. Adding entities to a rule may lead to the possibility of accidentally generating utterances that were not expected in a particular case and may be confused with the utterances specific to some other case that would affect the accuracy of the model. That may be avoided by separating different types of utterances in accordance with their common patterns of extension (like imperative and “wishful” sentences). Or even by creating separate grammars for separate cases with different priorities.  
2. Adding new rules to handle the complexity of separate rules may lead to the large volume of a grammar file, which to some extent can be handled through imports and multiple grammar files.  
3. Also grammars need to explicitly include possible outcomes and can’t reserve a space in the rule for “some input” between specific entities. I assume that this may be handled with preprocessing of the input.    
  

### Task 2: localizing the JSGF grammar in Russian

[JSGF text file](https://github.com/TianaQ/nlu-challenge/blob/master/JSGF_ru_ext.txt), [test script in Python](https://github.com/TianaQ/nlu-challenge/blob/master/test_ru.py)  

##### Examples covered by the localized grammar:  

> включи radio head  
> я хочу послушать paranoid android  
> поставь что-нибудь из джаза   
> поставь пожалуйста что-то из рока 
> мы хотим послушать джазовую музыку  
> включи рок музыку пожалуйста  
> поставь let it be битлз  
> включи что-нибудь из битлов  
> я хочу послушать альбом уммагумма группы пинк флойд 
> мы хотим послушать что-нибудь из группы cake  

In this task I had to proceed with a lot of assumptions as I couldn't find an example of a JSGF file for Russian to use as a reference.  
1. The input format is unknown, so I assumed that it may be a mix of cyrillic and latin characters because utf-8 encoding allows that.   
2. However if the input is cyrillic only, then the English names of music entities also should be adapted. I also assume that they may be processed separately and automatically to build a dictionary of suitable Russian equivalents.  
3. It also may be useful to take into account how original names in English tend to change in Russian informal speech, for example acquiring endings in accordance with Russian cases.  
4. Also I assumed that no preprocessing was applied to the input so possible word forms should be included in grammar rules for coverage.  

If any of my assumptions are not correct, please, let me know. I’ll make corrections in accordance with limitations provided.  

---

### Update

My initial approach to the challenge was from the recognition point of view so my grammars were aimed at correctly identifying a phrase, received as voice input, through the rules. From the point of generation there is an issue of possible combinations. So, for example, not just a pattern `"<album> by <artist>"`, but a specific match of an album and the artist, that is the author. I'm not sure if it should be handled on the grammar level.  
In Russian it also becomes necessary to build proper sequences of rules to handle word forms, for example gender, number and case for nouns together with the forms of corresponding adjectives and pronouns. It also may require splitting the entities grouped by meaning (like `<genre>`) into subgroups based on gender ("рок, метал" - "классика, прилагательное + музыка" - "техно"). Also, one word name entities from foreign languages may acquire grammar features in accordance with Russian grammar, and also native Russian names will be changing forms accordingly. I assume that some style guides may exist to better arrange such a grammar file.  
The only thing I didn't fully eliminate is the occasional "too many please" generations.  
