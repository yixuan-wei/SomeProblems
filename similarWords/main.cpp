/* Given a word, return the words with same components but different order
 * cases: word in vocabulary: signal true, lenOfArray 0;
 *          not in vocabulary: but has similar words: signal true, array return all satisfying words, lenOfArray>0
 *                              has no similar words: signal false, lenOfArray 0
 * Author: Yixuan Wei
 * 2018.8.4
 * */

#include <iostream>
#include <list>
#include <unordered_map>

using namespace std;
// T -> [], F -> [T], F -> [T,T,...], F->[**]

struct SimilarWordPosition{
    bool signal = false;
    u_long lenOfArray = 0;
    list<string> array;
};

string CalculateWordKey(const string & word){
    string result;
    int count [26]={0};
    //count letters
    for(auto letter:word){
        count[tolower(letter)-'a']++;
    }
    //generate key for word, ie. 1a4b6e
    for(int i=0;i<word.length();i++){
        if(count[i]!=0){
            result+=char(count[i]);
            result+=char(int('a')+i);
        }
    }
    return result;
}
// STL
SimilarWordPosition FindSimilarOfPosition(const string & target, const list<string> & vocabulary)
{
// read list to build up the hashmap
    unordered_map<string, list<string>> wordDict;
    for(auto & word:vocabulary){
        wordDict[CalculateWordKey(word)].push_back(word);
    }
    //find target in hashmap (find existing similar words)
    auto inHashMap =  wordDict.find(CalculateWordKey(target));
    SimilarWordPosition result;
    if(inHashMap==wordDict.end()){
        result.signal=false;
    } else{
        //find target in vocabulary
        auto inList = find(inHashMap->second.begin(),inHashMap->second.end(),target);
        result.signal=true;
        if(inList==inHashMap->second.end()){
            result.lenOfArray=inHashMap->second.size();
            result.array = inHashMap->second;
        }
        else{
            result.lenOfArray=0;
        }
    }
    return result;
}

int main(){
    list<string> vocabulary;
    vocabulary.emplace_back("abcd");
    vocabulary.emplace_back("bacd");
    SimilarWordPosition SWP = FindSimilarOfPosition("acdb",vocabulary);
    cout<<SWP.signal<<" "<<SWP.lenOfArray<<" ";
    for(auto & each:SWP.array){
        cout<<each<<" ";
    }
    return 0;
};