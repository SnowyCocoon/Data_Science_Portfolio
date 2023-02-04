# Symulowanie_Wizualne
Dane wykorzystane w uczeniu sieci neuronowych:
- (dwa gatunki drzew) https://drive.google.com/file/d/120tKA9UmObU0lxjRG1keFxknlX1SpxAt/view?usp=sharing
- (1 vs pozostałe gatunki drzew) https://drive.google.com/file/d/1Np4sMqw_7AwmATU4JmN5vStMEybzys9x/view

Wytrenowane modele:
- (dwa gatunki drzew) https://drive.google.com/file/d/1_bcNhmMh9ERirbR0S81ev5C4dWgq8v26/view?usp=sharing
- (1 vs pozostałe gatunki drzew) https://drive.google.com/file/d/1XIVRyTqff-gSci5Ag1SPowHSfBXYp9xr/view?usp=sharing
- (1 vs pozostałe gatunki drzew - Wersja Dominikowa) https://drive.google.com/file/d/15X3CEMdaxRqa0kgetRRHVwKDT27b5V2U/view?usp=sharing

|typ modelu|typ sieci|test acc|train acc|
|---|---|---|---|
|1 vs 1 (zbiór 1, podejście 1)|zwykła sieć neuronowa|0.8514|1.0|
|1 vs 1 (zbiór 1, podejście 1)|CNN|1.0|1.0|
|1 vs all (zbiór 2, podejście 1)|zwykła sieć neuronowa|0.56|0.6633|
|1 vs all (zbiór 2, podejście 1)|CNN|0.7706|0.9868|
|1 vs all (zbiór 2, podejście Dominikowe)|CNN|0.8478|1.0|
