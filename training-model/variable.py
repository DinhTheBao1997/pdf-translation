train_urls = [
    # train
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastritis-and-peptic-ulcer-disease/erosive-gastritis",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/b%E1%BB%87nh-vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-v%C3%A0-lo%C3%A9t-d%E1%BA%A1-d%C3%A0y/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-%C4%83n-m%C3%B2n",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E8%83%83%E7%82%8E%E3%81%8A%E3%82%88%E3%81%B3%E6%B6%88%E5%8C%96%E6%80%A7%E6%BD%B0%E7%98%8D/%E3%81%B3%E3%82%89%E3%82%93%E6%80%A7%E8%83%83%E7%82%8E?ruleredirectid=24"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastritis-and-peptic-ulcer-disease/nonerosive-gastritis",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/b%E1%BB%87nh-vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-v%C3%A0-lo%C3%A9t-d%E1%BA%A1-d%C3%A0y/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-kh%C3%B4ng-%C4%83n-m%C3%B2n",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e8%83%83%e7%82%8e%e3%81%8a%e3%82%88%e3%81%b3%e6%b6%88%e5%8c%96%e6%80%a7%e6%bd%b0%e7%98%8d/%e9%9d%9e%e3%81%b3%e3%82%89%e3%82%93%e6%80%a7%e8%83%83%e7%82%8e"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastroenteritis/drug-related-gastroenteritis-and-chemical-related-gastroenteritis",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t-do-ru%E1%BB%99t-v%C3%A0-vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t-do-ho%C3%A1-ch%E1%BA%A5t",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e8%83%83%e8%85%b8%e7%82%8e/%e8%96%ac%e7%89%a9%e9%96%a2%e9%80%a3%e8%83%83%e8%85%b8%e7%82%8e%e3%81%8a%e3%82%88%e3%81%b3%e5%8c%96%e5%ad%a6%e7%89%a9%e8%b3%aa%e9%96%a2%e9%80%a3%e8%83%83%e8%85%b8%e7%82%8e"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastroenteritis/overview-of-gastroenteritis",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/vi%c3%aam-d%e1%ba%a1-d%c3%a0y-ru%e1%bb%99t/t%e1%bb%95ng-quan-v%e1%bb%81-vi%c3%aam-d%e1%ba%a1-d%c3%a0y-ru%e1%bb%99t",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e8%83%83%e8%85%b8%e7%82%8e/%e8%83%83%e8%85%b8%e7%82%8e"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastroenteritis/e-coli-gastroenteritis",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t-do-e-coli",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/13-%e6%84%9f%e6%9f%93%e6%80%a7%e7%96%be%e6%82%a3/%e3%82%b0%e3%83%a9%e3%83%a0%e9%99%b0%e6%80%a7%e6%a1%bf%e8%8f%8c/%e5%a4%a7%e8%85%b8%e8%8f%8c-%e6%84%9f%e6%9f%93%e7%97%87"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastroenteritis/norovirus-gastroenteritis",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/vi%c3%aam-d%e1%ba%a1-d%c3%a0y-ru%e1%bb%99t/vi%c3%aam-d%e1%ba%a1-d%c3%a0y-ru%e1%bb%99t-do-norovirus",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e8%83%83%e8%85%b8%e7%82%8e/%e8%83%83%e8%85%b8%e7%82%8e"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastroenteritis/rotavirus-gastroenteritis",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t-do-rotavirus",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e8%83%83%e8%85%b8%e7%82%8e/%e8%83%83%e8%85%b8%e7%82%8e"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastroenteritis/staphylococcal-food-poisoning",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/vi%c3%aam-d%e1%ba%a1-d%c3%a0y-ru%e1%bb%99t/ng%e1%bb%99-%c4%91%e1%bb%99c-th%e1%bb%b1c-ph%e1%ba%a9m-do-%c4%91%e1%bb%99c-t%e1%bb%91-t%e1%bb%a5-c%e1%ba%a7u",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e8%83%83%e8%85%b8%e7%82%8e/%e8%83%83%e8%85%b8%e7%82%8e"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/gastroenteritis/traveler%e2%80%99s-diarrhea",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/vi%C3%AAm-d%E1%BA%A1-d%C3%A0y-ru%E1%BB%99t/ti%C3%AAu-ch%E1%BA%A3y-%E1%BB%9F-kh%C3%A1ch-du-l%E1%BB%8Bch",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e8%83%83%e8%85%b8%e7%82%8e/%e6%97%85%e8%a1%8c%e8%80%85%e4%b8%8b%e7%97%a2%e7%97%87"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/approach-to-the-gastrointestinal-patient/evaluation-of-the-gastrointestinal-patient",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/ti%E1%BA%BFp-c%E1%BA%ADn-b%E1%BB%87nh-nh%C3%A2n-c%C3%B3-b%E1%BB%87nh-l%C3%BD-ti%C3%AAu-h%C3%B3a/%C4%91%C3%A1nh-gi%C3%A1-b%E1%BB%87nh-nh%C3%A2n-c%C3%B3-b%E1%BB%87nh-l%C3%BD-ti%C3%AAu-h%C3%B3a",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%82%92%e6%9c%89%e3%81%99%e3%82%8b%e6%82%a3%e8%80%85%e3%81%b8%e3%81%ae%e3%82%a2%e3%83%97%e3%83%ad%e3%83%bc%e3%83%81/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e6%82%a3%e8%80%85%e3%81%ae%e8%a9%95%e4%be%a1"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/approach-to-the-gastrointestinal-patient/disorders-of-gut-brain-interaction",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/ti%e1%ba%bfp-c%e1%ba%adn-b%e1%bb%87nh-nh%c3%a2n-c%c3%b3-b%e1%bb%87nh-l%c3%bd-ti%c3%aau-h%c3%b3a/b%e1%bb%87nh-l%c3%bd-ti%c3%aau-h%c3%b3a-ch%e1%bb%a9c-n%c4%83ng",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%82%92%e6%9c%89%e3%81%99%e3%82%8b%e6%82%a3%e8%80%85%e3%81%b8%e3%81%ae%e3%82%a2%e3%83%97%e3%83%ad%e3%83%bc%e3%83%81/%e6%a9%9f%e8%83%bd%e6%80%a7%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/chronic-abdominal-pain-and-recurrent-abdominal-pain",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/tri%E1%BB%87u-ch%E1%BB%A9ng-c%E1%BB%A7a-c%C3%A1c-t%C3%ACnh-tr%E1%BA%A1ng-b%E1%BA%A5t-th%C6%B0%E1%BB%9Dng-%E1%BB%9F-%C4%91%C6%B0%E1%BB%9Dng-ti%C3%AAu-h%C3%B3a/%C4%91au-b%E1%BB%A5ng-m%E1%BA%A1n-t%C3%ADnh-v%C3%A0-%C4%91au-b%E1%BB%A5ng-t%C3%A1i-ph%C3%A1t",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e6%85%a2%e6%80%a7%e8%85%b9%e7%97%9b%e3%81%8a%e3%82%88%e3%81%b3%e5%8f%8d%e5%be%a9%e6%80%a7%e8%85%b9%e7%97%9b"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/dyspepsia",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/tri%e1%bb%87u-ch%e1%bb%a9ng-c%e1%bb%a7a-c%c3%a1c-t%c3%acnh-tr%e1%ba%a1ng-b%e1%ba%a5t-th%c6%b0%e1%bb%9dng-%e1%bb%9f-%c4%91%c6%b0%e1%bb%9dng-ti%c3%aau-h%c3%b3a/kh%c3%b3-ti%c3%aau",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e6%b6%88%e5%8c%96%e4%b8%8d%e8%89%af"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/hiccups",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/tri%E1%BB%87u-ch%E1%BB%A9ng-c%E1%BB%A7a-c%C3%A1c-t%C3%ACnh-tr%E1%BA%A1ng-b%E1%BA%A5t-th%C6%B0%E1%BB%9Dng-%E1%BB%9F-%C4%91%C6%B0%E1%BB%9Dng-ti%C3%AAu-h%C3%B3a/n%E1%BA%A5c",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e5%90%83%e9%80%86"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/lump-in-throat",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/tri%e1%bb%87u-ch%e1%bb%a9ng-c%e1%bb%a7a-c%c3%a1c-t%c3%acnh-tr%e1%ba%a1ng-b%e1%ba%a5t-th%c6%b0%e1%bb%9dng-%e1%bb%9f-%c4%91%c6%b0%e1%bb%9dng-ti%c3%aau-h%c3%b3a/c%e1%bb%a5c-trong-h%e1%bb%8dng",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e5%92%bd%e5%96%89%e9%a0%ad%e7%95%b0%e5%b8%b8%e6%84%9f"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/nausea-and-vomiting",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/tri%E1%BB%87u-ch%E1%BB%A9ng-c%E1%BB%A7a-c%C3%A1c-t%C3%ACnh-tr%E1%BA%A1ng-b%E1%BA%A5t-th%C6%B0%E1%BB%9Dng-%E1%BB%9F-%C4%91%C6%B0%E1%BB%9Dng-ti%C3%AAu-h%C3%B3a/bu%E1%BB%93n-n%C3%B4n-v%C3%A0-n%C3%B4n",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e6%82%aa%e5%bf%83%e3%81%8a%e3%82%88%e3%81%b3%e5%98%94%e5%90%90"
    },
]
test_urls = [
    # test
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/rumination",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/tri%e1%bb%87u-ch%e1%bb%a9ng-c%e1%bb%a7a-c%c3%a1c-t%c3%acnh-tr%e1%ba%a1ng-b%e1%ba%a5t-th%c6%b0%e1%bb%9dng-%e1%bb%9f-%c4%91%c6%b0%e1%bb%9dng-ti%c3%aau-h%c3%b3a/nhai-l%e1%ba%a1i",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e5%8f%8d%e8%8a%bb%e7%97%87"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/constipation",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/tri%E1%BB%87u-ch%E1%BB%A9ng-c%E1%BB%A7a-c%C3%A1c-t%C3%ACnh-tr%E1%BA%A1ng-b%E1%BA%A5t-th%C6%B0%E1%BB%9Dng-%E1%BB%9F-%C4%91%C6%B0%E1%BB%9Dng-ti%C3%AAu-h%C3%B3a/t%C3%A1o-b%C3%B3n",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e4%be%bf%e7%a7%98"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/diarrhea",
        "vi": "https://www.msdmanuals.com/vi/chuy%c3%aan-gia/r%e1%bb%91i-lo%e1%ba%a1n-ti%c3%aau-h%c3%b3a/tri%e1%bb%87u-ch%e1%bb%a9ng-c%e1%bb%a7a-c%c3%a1c-t%c3%acnh-tr%e1%ba%a1ng-b%e1%ba%a5t-th%c6%b0%e1%bb%9dng-%e1%bb%9f-%c4%91%c6%b0%e1%bb%9dng-ti%c3%aau-h%c3%b3a/b%e1%bb%87nh-ti%c3%aau-ch%e1%ba%a3y",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e4%b8%8b%e7%97%a2"
    },
    {
        "en": "https://www.msdmanuals.com/professional/gastrointestinal-disorders/symptoms-of-gastrointestinal-disorders/gas-related-complaints",
        "vi": "https://www.msdmanuals.com/vi/chuy%C3%AAn-gia/r%E1%BB%91i-lo%E1%BA%A1n-ti%C3%AAu-h%C3%B3a/tri%E1%BB%87u-ch%E1%BB%A9ng-c%E1%BB%A7a-c%C3%A1c-t%C3%ACnh-tr%E1%BA%A1ng-b%E1%BA%A5t-th%C6%B0%E1%BB%9Dng-%E1%BB%9F-%C4%91%C6%B0%E1%BB%9Dng-ti%C3%AAu-h%C3%B3a/tri%E1%BB%87u-ch%E1%BB%A9ng-li%C3%AAn-quan-%C4%91%E1%BA%BFn-h%C6%A1i",
        "ja": "https://www.msdmanuals.com/ja-jp/%e3%83%97%e3%83%ad%e3%83%95%e3%82%a7%e3%83%83%e3%82%b7%e3%83%a7%e3%83%8a%e3%83%ab/01-%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3/%e6%b6%88%e5%8c%96%e7%ae%a1%e7%96%be%e6%82%a3%e3%81%ae%e7%97%87%e7%8a%b6/%e3%82%ac%e3%82%b9%e3%81%ab%e9%96%a2%e9%80%a3%e3%81%99%e3%82%8b%e6%84%81%e8%a8%b4"
    },
]
