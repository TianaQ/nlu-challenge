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
> поставь пожалуйста какой-нибудь рок  
> мы хотим послушать джазовую музыку  
> включи какую-нибудь рок музыку пожалуйста  
> поставь let it be битлз  
> включи что-нибудь из битлов  
> я хочу послушать умагуму пинк флойд  
> мы хотим послушать что-нибудь из группы cake  

In this task I had to proceed with a lot of assumptions as I couldn't find an example of a JSGF file for Russian to use as a reference.  
1. The input format is unknown, so I assumed that it may be a mix of cyrillic and latin characters because utf-8 encoding allows that.   
2. However if the input is cyrillic only, then the English names of music entities also should be adapted. I also assume that they may be processed separately and automatically to build a dictionary of suitable Russian equivalents.  
3. It also may be useful to take into account how original names in English tend to change in Russian informal speech, for example acquiring endings in accordance with Russian cases.  
4. Also I assumed that no preprocessing was applied to the input so possible word forms should be included in grammar rules for coverage.  

If any of my assumptions are not correct, please, let me know. I’ll make corrections in accordance with limitations provided.  
