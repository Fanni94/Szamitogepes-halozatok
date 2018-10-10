**Számítógépes hálózatok feladat**

- Kliens-szerver alkalmazás, ahol a kliens a hallgató, szerver a neptun. TCP alapú. Hallgató tudjon jelentkezni a vizsgára: "vizsga, neptun1, vizsga1" elküldésével, ahol a vizsga a parancs, neptun1 a hallgató azonosítója, a vizsga1 a vizsgaidőpont. A neptun egy randomszámmal válaszol 1 és 5 között random.randint(1, 5).

- Készíts egy Tanár alkalmazást, amely lecseréli a neptun rendszerben szereplő random jegy adást. Amikor egy hallgató jelentkezik egy vizsgára, akkor a Neptun küldje tovább ezt a jelentkezést UDP kommunikáción keresztül a Tanár szervernek. A Tanár szerver küldje vissza a Neptunnak az eredményt, amely visszaküldi a Hallgatónak.

- Ha a hallgató nem elégedett a jegyével, akkor tudjon reklamálni. Ha a jegy, amit kapot kisebb, mint 3, akkor küldjön egy üzenetet közvetlenül a Tanárnak: "reklamalok". Ha 4 vagy 5 jegyet szerzett, akkor küldje el az "elfogadom" üzenetet, amelyre a Tanár válaszoljon egy "OK" üzenettel.