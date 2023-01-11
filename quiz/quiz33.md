### 
       def translate_dna(in_protein:str)-> str :
    mapping = {"A":"T","G":"C","T":"A","C":"G"}
    if in_protein in mapping :
        out_protein = mapping[in_protein]
    else :
        out_protein = "not valid"

    return out_protein
       from main import translate_dna 
       import pytest
    # every test case is  a function
    def test_a_to_t():
        assert translate_dna("C") == "G"
    def test_not_valid():
        assert translate_dna("Z") == "not valid"






![Screen Shot 2023-01-11 at 22 51 19](https://user-images.githubusercontent.com/112072887/211823271-66fb6547-37c5-4d95-bb8b-9057f978e861.png)
