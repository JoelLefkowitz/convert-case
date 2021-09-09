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
