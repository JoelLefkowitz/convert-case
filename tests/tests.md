# Test cases

| test     | lower    | upper    | sentence | title    | camel  | snake    | kebab    | pascal |
| -------- | -------- | -------- | -------- | -------- | ------ | -------- | -------- | ------ |
| a        | a        | A        | A        | A        | a      | a        | a        | A      |
| A        | a        | A        | A        | A        | a      | a        | a        | A      |
| abc      | abc      | ABC      | Abc      | Abc      | abc    | abc      | abc      | Abc    |
| ab cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| Ab cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| Ab Cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ab_cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ab-cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| abCd     | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ABCD     | abcd     | ABCD     | Abcd     | Abcd     | abcd   | abcd     | abcd     | Abcd   |
| AbCd     | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ab cd ef | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |
| AbCdEf   | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |
| ab-cd-ef | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |
| Ab cd ef | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |
| 1        | 1        | 1        | 1        | 1        | 1      | 1        | 1        | 1      |
| 1bc      | 1bc      | 1BC      | 1bc      | 1bc      | 1bc    | 1bc      | 1bc      | 1bc    |
| a1c      | a1c      | A1C      | A1c      | A1c      | a1c    | a1c      | a1c      | A1c    |
| ab1      | ab1      | AB1      | Ab1      | Ab1      | ab1    | ab1      | ab1      | Ab1    |
| a1 c     | a1 c     | A1 C     | A1 c     | A1 C     | a1C    | a1_c     | a1-c     | A1C    |
| a1-c     | a1 c     | A1 C     | A1 c     | A1 C     | a1C    | a1_c     | a1-c     | A1C    |
