train_urls = [
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng/gi%E1%BB%9Bi-thi%E1%BB%87u-ph%C6%B0%C6%A1ng-ph%C3%A1p-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/approach-to-the-critically-ill-patient/introduction-to-the-approach-to-the-critically-ill-patient",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E5%BA%8F%E8%AB%96"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng/theo-d%C3%B5i-v%C3%A0-x%C3%A9t-nghi%E1%BB%87m-tr%C3%AAn-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/approach-to-the-critically-ill-patient/monitoring-and-testing-the-critical-care-patient",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81/%E9%9B%86%E4%B8%AD%E6%B2%BB%E7%99%82%E3%81%8C%E5%BF%85%E8%A6%81%E3%81%AA%E6%82%A3%E8%80%85%E3%81%AE%E3%83%A2%E3%83%8B%E3%82%BF%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%8A%E3%82%88%E3%81%B3%E6%A4%9C%E6%9F%BB"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng/h%E1%BB%87-th%E1%BB%91ng-thang-%C4%91i%E1%BB%83m-trong-ch%C4%83m-s%C3%B3c-t%C3%ADch-c%E1%BB%B1c",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/approach-to-the-critically-ill-patient/critical-care-scoring-systems",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81/%E9%9B%86%E4%B8%AD%E6%B2%BB%E7%99%82%E3%81%AE%E3%82%B9%E3%82%B3%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng/ti%E1%BA%BFp-c%E1%BA%ADn-m%E1%BA%A1ch-m%C3%A1u",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/approach-to-the-critically-ill-patient/vascular-access",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81/%E8%A1%80%E7%AE%A1%E7%A2%BA%E4%BF%9D"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng/gi%E1%BA%A3m-b%C3%A3o-h%C3%B2a-oxy",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/approach-to-the-critically-ill-patient/oxygen-desaturation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81/%E9%85%B8%E7%B4%A0%E9%A3%BD%E5%92%8C%E5%BA%A6%E3%81%AE%E4%BD%8E%E4%B8%8B"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng/thi%E1%BB%83u-ni%E1%BB%87u",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/approach-to-the-critically-ill-patient/oliguria",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81/%E4%B9%8F%E5%B0%BF"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn-%C4%91i%E1%BB%81u-tr%E1%BB%8B-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng/k%C3%ADch-%C4%91%E1%BB%99ng,-l%C3%BA-l%E1%BA%ABn,-v%C3%A0-thu%E1%BB%91c-ch%E1%BA%B9n-th%E1%BA%A7n-kinh-c%C6%A1-%E1%BB%9F-b%E1%BB%87nh-nh%C3%A2n-b%E1%BB%8B-b%E1%BB%87nh-n%E1%BA%B7ng",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/approach-to-the-critically-ill-patient/agitation,-confusion,-and-neuromuscular-blockade-in-critically-ill-patients",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%B8%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81/%E9%87%8D%E7%97%87-critically-ill-%E6%82%A3%E8%80%85%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E8%88%88%E5%A5%AE-%E9%8C%AF%E4%B9%B1-%E3%81%8A%E3%82%88%E3%81%B3%E7%A5%9E%E7%B5%8C%E7%AD%8B%E6%8E%A5%E5%90%88%E9%83%A8%E9%81%AE%E6%96%AD"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-tim-v%C3%A0-c%E1%BA%A5p-c%E1%BB%A9u-ng%E1%BB%ABng-tu%E1%BA%A7n-ho%C3%A0n/ng%E1%BB%ABng-tim",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/cardiac-arrest-and-cpr/cardiac-arrest",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%BF%83%E5%81%9C%E6%AD%A2%E3%81%8A%E3%82%88%E3%81%B3cpr/%E5%BF%83%E5%81%9C%E6%AD%A2"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-tim-v%C3%A0-c%E1%BA%A5p-c%E1%BB%A9u-ng%E1%BB%ABng-tu%E1%BA%A7n-ho%C3%A0n/h%E1%BB%93i-sinh-tim-ph%E1%BB%95i-cpr-%E1%BB%9F-ng%C6%B0%E1%BB%9Di-l%E1%BB%9Bn",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/cardiac-arrest-and-cpr/cardiopulmonary-resuscitation-cpr-in-adults",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%BF%83%E5%81%9C%E6%AD%A2%E3%81%8A%E3%82%88%E3%81%B3cpr/%E6%88%90%E4%BA%BA%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%BF%83%E8%82%BA%E8%98%87%E7%94%9F-cpr"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-tim-v%C3%A0-c%E1%BA%A5p-c%E1%BB%A9u-ng%E1%BB%ABng-tu%E1%BA%A7n-ho%C3%A0n/h%E1%BB%93i-sinh-tim-ph%E1%BB%95i-cpr-%E1%BB%9F-tr%E1%BA%BB-s%C6%A1-sinh-v%C3%A0-tr%E1%BA%BB-nh%E1%BB%8F",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/cardiac-arrest-and-cpr/cardiopulmonary-resuscitation-cpr-in-infants-and-children",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%BF%83%E5%81%9C%E6%AD%A2%E3%81%8A%E3%82%88%E3%81%B3cpr/%E4%B9%B3%E5%85%90%E3%81%8A%E3%82%88%E3%81%B3%E5%B0%8F%E5%85%90%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%BF%83%E8%82%BA%E8%98%87%E7%94%9F-cpr"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-c%C6%A1-b%E1%BA%A3n/th%E1%BB%B1c-hi%E1%BB%87n-b%C3%B3p-b%C3%B3ng-qua-m%E1%BA%B7t-n%E1%BA%A1-nh%C6%B0-th%E1%BA%BF-n%C3%A0o",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-basic-airway-procedures/how-to-do-bag-valve-mask-bvm-ventilation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E3%83%90%E3%83%83%E3%82%B0%E3%83%90%E3%83%AB%E3%83%96%E3%83%9E%E3%82%B9%E3%82%AF%E6%8F%9B%E6%B0%97"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-c%C6%A1-b%E1%BA%A3n/th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-%C4%91%E1%BB%99ng-t%C3%A1c-n%C3%A2ng-cao-%C4%91%E1%BA%A7u-v%C3%A0-%C4%91%E1%BA%A9y-h%C3%A0m-nh%C6%B0-th%E1%BA%BF-n%C3%A0o",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-basic-airway-procedures/how-to-do-head-tilt-chin-lift-and-jaw-thrust-maneuvers",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E9%A0%AD%E9%83%A8%E5%BE%8C%E5%B1%88%E3%81%82%E3%81%94%E5%85%88%E6%8C%99%E4%B8%8A%E6%B3%95%E3%81%8A%E3%82%88%E3%81%B3%E4%B8%8B%E9%A1%8E%E6%8C%99%E4%B8%8A%E6%B3%95"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-c%C6%A1-b%E1%BA%A3n/l%C3%A0m-th%E1%BA%BF-n%C3%A0o-%C4%91%E1%BB%83-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-%C4%91%E1%BB%99ng-t%C3%A1c-heimlich-%E1%BB%9F-ng%C6%B0%E1%BB%9Di-l%E1%BB%9Bn-t%E1%BB%89nh-t%C3%A1o",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-basic-airway-procedures/how-to-do-the-heimlich-maneuver-in-the-conscious-adult-or-child",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E6%84%8F%E8%AD%98%E3%81%AE%E3%81%82%E3%82%8B%E6%88%90%E4%BA%BA%E3%81%BE%E3%81%9F%E3%81%AF%E5%B0%8F%E5%85%90%E3%81%AB%E5%AF%BE%E3%81%99%E3%82%8B%E3%83%8F%E3%82%A4%E3%83%A0%E3%83%AA%E3%83%83%E3%83%92%E6%B3%95"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-c%C6%A1-b%E1%BA%A3n/l%C3%A0m-th%E1%BA%BF-n%C3%A0o-%C4%91%E1%BB%83-%C4%91%E1%BA%B7t-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-m%C5%A9i-h%E1%BB%8Dng",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-basic-airway-procedures/how-to-insert-a-nasopharyngeal-airway",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E7%B5%8C%E9%BC%BB%E3%82%A8%E3%82%A2%E3%82%A6%E3%82%A7%E3%82%A4%E3%81%AE%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-c%C6%A1-b%E1%BA%A3n/l%C3%A0m-th%E1%BA%BF-n%C3%A0o-%C4%91%E1%BB%83-%C4%91%E1%BA%B7t-canuyn-mi%E1%BB%87ng",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-basic-airway-procedures/how-to-insert-an-oropharyngeal-airway",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E7%B5%8C%E5%8F%A3%E3%82%A8%E3%82%A2%E3%82%A6%E3%82%A7%E3%82%A4%E3%81%AE%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-c%C6%A1-b%E1%BA%A3n/c%C3%A1ch-%C4%91i%E1%BB%81u-tr%E1%BB%8B-cho-tr%E1%BA%BB-s%C6%A1-sinh-ngh%E1%BA%B9t-th%E1%BB%9F",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-basic-airway-procedures/how-to-treat-the-choking-conscious-infant",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E6%84%8F%E8%AD%98%E3%81%AE%E3%81%82%E3%82%8B%E4%B9%B3%E5%85%90%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E7%AA%92%E6%81%AF%E3%81%AE%E6%B2%BB%E7%99%82%E6%96%B9%E6%B3%95"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-kh%C3%A1c/c%C3%A1ch-m%E1%BB%9F-s%E1%BB%A5n-nh%E1%BA%ABn-gi%C3%A1p-qua-da",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-airway-procedures/how-to-do-a-percutaneous-cricothyrotomy",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E7%B5%8C%E7%9A%AE%E7%9A%84%E8%BC%AA%E7%8A%B6%E7%94%B2%E7%8A%B6%E9%96%93%E8%86%9C%EF%BC%88%E9%9D%B1%E5%B8%AF%EF%BC%89%E5%88%87%E9%96%8B%E3%83%BB%E7%A9%BF%E5%88%BA"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-kh%C3%A1c/th%C3%B4ng-kh%C3%AD-%C3%A1p-l%E1%BB%B1c-d%C6%B0%C6%A1ng-kh%C3%B4ng-x%C3%A2m-nh%E1%BA%ADp-nh%C6%B0-th%E1%BA%BF-n%C3%A0o",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-airway-procedures/how-to-do-noninvasive-positive-pressure-ventilation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E9%9D%9E%E4%BE%B5%E8%A5%B2%E7%9A%84%E9%99%BD%E5%9C%A7%E6%8F%9B%E6%B0%97"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-kh%C3%A1c/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-%C4%91%E1%BA%B7t-n%E1%BB%99i-kh%C3%AD-qu%E1%BA%A3n-%C4%91%C6%B0%E1%BB%9Dng-mi%E1%BB%87ng-b%E1%BA%B1ng-c%C3%A1ch-s%E1%BB%AD-d%E1%BB%A5ng-%C4%91%C3%A8n-soi-thanh-qu%E1%BA%A3n-c%C3%B3-video",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-airway-procedures/how-to-do-orotracheal-intubation-using-video-laryngoscopy",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E3%83%93%E3%83%87%E3%82%AA%E5%96%89%E9%A0%AD%E9%8F%A1%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E7%B5%8C%E5%8F%A3%E6%B0%97%E7%AE%A1%E6%8C%BF%E7%AE%A1"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-kh%C3%A1c/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-hai-l%C3%B2ng-th%E1%BB%B1c-qu%E1%BA%A3n-kh%C3%AD-qu%E1%BA%A3n-combitube-ho%E1%BA%B7c-%E1%BB%91ng-thanh-qu%E1%BA%A3n-king",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-airway-procedures/how-to-insert-an-esophageal-tracheal-double-lumen-tube-combitube-or-a-king-laryngeal-tube",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E9%A3%9F%E9%81%93%E3%83%BB%E6%B0%97%E7%AE%A1%E7%94%A8%E3%83%80%E3%83%96%E3%83%AB%E3%83%AB%E3%83%BC%E3%83%A1%E3%83%B3%E3%83%81%E3%83%A5%E3%83%BC%E3%83%96%EF%BC%88combitube%C2%AE%EF%BC%89%E3%81%BE%E3%81%9F%E3%81%AF%E3%83%A9%E3%83%AA%E3%83%B3%E3%82%B8%E3%82%A2%E3%83%AB%E3%83%81%E3%83%A5%E3%83%BC%E3%83%96%E3%81%AE%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-kh%C3%A1c/c%C3%A1ch-%C4%91%E1%BA%B7t-mask-thanh-qu%E1%BA%A3n",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-airway-procedures/how-to-insert-a-laryngeal-mask-airway",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E6%B0%97%E9%81%93%E5%87%A6%E7%BD%AE/%E3%83%A9%E3%83%AA%E3%83%B3%E3%82%B8%E3%82%A2%E3%83%AB%E3%83%9E%E3%82%B9%E3%82%AF%E3%81%AE%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-m%E1%BA%A1ch-m%C3%A1u-trung-t%C3%A2m/c%C3%A1ch-%C4%91%E1%BA%B7t-cannun-%C4%91%E1%BB%99ng-m%E1%BA%A1ch-%C4%91%C3%B9i-c%C3%B3-d%E1%BA%ABn-h%C6%B0%E1%BB%9Bng-b%E1%BA%B1ng-si%C3%AAu-%C3%A2m",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-central-vascular-procedures/how-to-do-femoral-artery-cannulation,-ultrasound-guided",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E4%B8%AD%E5%BF%83%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E3%81%AE%E5%87%A6%E7%BD%AE/%E8%B6%85%E9%9F%B3%E6%B3%A2%E3%82%AC%E3%82%A4%E3%83%89%E4%B8%8B%E5%A4%A7%E8%85%BF%E5%8B%95%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-m%E1%BA%A1ch-m%C3%A1u-trung-t%C3%A2m/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-%C4%91%C3%B9i",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-central-vascular-procedures/how-to-do-femoral-vein-cannulation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E4%B8%AD%E5%BF%83%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E3%81%AE%E5%87%A6%E7%BD%AE/%E5%A4%A7%E8%85%BF%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-m%E1%BA%A1ch-m%C3%A1u-trung-t%C3%A2m/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-%C4%91%C3%B9i-c%C3%B3-d%E1%BA%ABn-h%C6%B0%E1%BB%9Bng-b%E1%BA%B1ng-si%C3%AAu-%C3%A2m",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-central-vascular-procedures/how-to-do-femoral-vein-cannulation,-ultrasound-guided",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E4%B8%AD%E5%BF%83%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E3%81%AE%E5%87%A6%E7%BD%AE/%E8%B6%85%E9%9F%B3%E6%B3%A2%E3%82%AC%E3%82%A4%E3%83%89%E4%B8%8B%E5%A4%A7%E8%85%BF%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-m%E1%BA%A1ch-m%C3%A1u-trung-t%C3%A2m/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-d%C6%B0%E1%BB%9Bi-%C4%91%C3%B2n-d%C6%B0%E1%BB%9Bi-x%C6%B0%C6%A1ng-%C4%91%C3%B2n",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-central-vascular-procedures/how-to-do-infraclavicular-subclavian-vein-cannulation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E4%B8%AD%E5%BF%83%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E3%81%AE%E5%87%A6%E7%BD%AE/%E9%8E%96%E9%AA%A8%E4%B8%8B%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81%E3%81%AB%E3%82%88%E3%82%8B%E9%8E%96%E9%AA%A8%E4%B8%8B%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-m%E1%BA%A1ch-m%C3%A1u-trung-t%C3%A2m/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-d%C6%B0%E1%BB%9Bi-%C4%91%C3%B2n-d%C6%B0%E1%BB%9Bi-x%C6%B0%C6%A1ng-%C4%91%C3%B2n-c%C3%B3-d%E1%BA%ABn-h%C6%B0%E1%BB%9Bng-si%C3%AAu-%C3%A2m",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-central-vascular-procedures/how-to-do-infraclavicular-subclavian-vein-cannulation,-ultrasound-guided",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E4%B8%AD%E5%BF%83%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E3%81%AE%E5%87%A6%E7%BD%AE/%E9%8E%96%E9%AA%A8%E4%B8%8B%E3%82%A2%E3%83%97%E3%83%AD%E3%83%BC%E3%83%81%E3%81%AB%E3%82%88%E3%82%8B%E8%B6%85%E9%9F%B3%E6%B3%A2%E3%82%AC%E3%82%A4%E3%83%89%E4%B8%8B%E9%8E%96%E9%AA%A8%E4%B8%8B%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-m%E1%BA%A1ch-m%C3%A1u-trung-t%C3%A2m/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-c%E1%BA%A3nh-trong",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-central-vascular-procedures/how-to-do-internal-jugular-vein-cannulation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E4%B8%AD%E5%BF%83%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E3%81%AE%E5%87%A6%E7%BD%AE/%E5%86%85%E9%A0%B8%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-m%E1%BA%A1ch-m%C3%A1u-trung-t%C3%A2m/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-c%E1%BA%A3nh-trong,-c%C3%B3-d%E1%BA%ABn-h%C6%B0%E1%BB%9Bng-b%E1%BA%B1ng-si%C3%AAu-%C3%A2m",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-central-vascular-procedures/how-to-do-internal-jugular-vein-cannulation,-ultrasound-guided",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E4%B8%AD%E5%BF%83%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E3%81%AE%E5%87%A6%E7%BD%AE/%E8%B6%85%E9%9F%B3%E6%B3%A2%E3%82%AC%E3%82%A4%E3%83%89%E4%B8%8B%E5%86%85%E9%A0%B8%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%E1%BB%9F-m%E1%BA%A1ch-m%C3%A1u-ngo%E1%BA%A1i-vi/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-trong-x%C6%B0%C6%A1ng-v%C3%A0-v%E1%BB%9Bi-m%C3%A1y-khoan-%C4%91i%E1%BB%87n",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-peripheral-vascular-procedures/how-to-do-intraosseous-cannulation,-manually-and-with-a-power-drill",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E5%87%A6%E7%BD%AE/%E9%AA%A8%E9%AB%84%E8%B7%AF%E7%A2%BA%E4%BF%9D%EF%BC%88%E7%94%A8%E6%89%8B%E7%9A%84%E6%89%8B%E6%8A%80%E3%81%8A%E3%82%88%E3%81%B3%E9%9B%BB%E5%8B%95%E3%83%89%E3%83%AA%E3%83%AB%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E6%89%8B%E6%8A%80%EF%BC%89"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%E1%BB%9F-m%E1%BA%A1ch-m%C3%A1u-ngo%E1%BA%A1i-vi/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-ngo%E1%BA%A1i-bi%C3%AAn",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-peripheral-vascular-procedures/how-to-do-peripheral-vein-cannulation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E5%87%A6%E7%BD%AE/%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%E1%BB%9F-m%E1%BA%A1ch-m%C3%A1u-ngo%E1%BA%A1i-vi/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-t%C4%A9nh-m%E1%BA%A1ch-ngo%E1%BA%A1i-bi%C3%AAn-c%C3%B3-d%E1%BA%ABn-h%C6%B0%E1%BB%9Bng-b%E1%BA%B1ng-si%C3%AAu-%C3%A2m",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-peripheral-vascular-procedures/how-to-do-peripheral-vein-cannulation,-ultrasound-guided",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E5%87%A6%E7%BD%AE/%E8%B6%85%E9%9F%B3%E6%B3%A2%E3%82%AC%E3%82%A4%E3%83%89%E4%B8%8B%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%E1%BB%9F-m%E1%BA%A1ch-m%C3%A1u-ngo%E1%BA%A1i-vi/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-%C4%91%E1%BB%99ng-m%E1%BA%A1ch-quay",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-peripheral-vascular-procedures/how-to-do-radial-artery-cannulation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E5%87%A6%E7%BD%AE/%E6%A9%88%E9%AA%A8%E5%8B%95%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%E1%BB%9F-m%E1%BA%A1ch-m%C3%A1u-ngo%E1%BA%A1i-vi/c%C3%A1ch-%C4%91%E1%BA%B7t-%E1%BB%91ng-th%C3%B4ng-%C4%91%E1%BB%99ng-m%E1%BA%A1ch-quay,-c%C3%B3-d%E1%BA%ABn-h%C6%B0%E1%BB%9Bng-si%C3%AAu-%C3%A2m",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-peripheral-vascular-procedures/how-to-do-radial-artery-cannulation,-ultrasound-guided",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E5%87%A6%E7%BD%AE/%E8%B6%85%E9%9F%B3%E6%B3%A2%E3%82%AC%E3%82%A4%E3%83%89%E4%B8%8B%E6%A9%88%E9%AA%A8%E5%8B%95%E8%84%88%E3%82%AB%E3%83%86%E3%83%BC%E3%83%86%E3%83%AB%E6%8C%BF%E5%85%A5"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-%E1%BB%9F-m%E1%BA%A1ch-m%C3%A1u-ngo%E1%BA%A1i-vi/c%C3%A1ch-l%E1%BA%A5y-m%E1%BA%ABu-m%C3%A1u-t%C4%A9nh-m%E1%BA%A1ch",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-peripheral-vascular-procedures/how-to-do-venous-blood-sampling",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E6%9C%AB%E6%A2%A2%E9%9D%99%E8%84%88%E7%AD%89%E3%81%AE%E8%A1%80%E7%AE%A1%E9%96%A2%E9%80%A3%E5%87%A6%E7%BD%AE/%E9%9D%99%E8%84%88%E8%A1%80%E3%81%AE%E6%8E%A1%E5%8F%96"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-c%E1%BA%A5p-c%E1%BB%A9u-kh%C3%A1c-trong-y-khoa/c%C3%A1ch-r%E1%BB%ADa-khoang-ph%C3%BAc-m%E1%BA%A1c-%C4%91%E1%BB%83-ch%E1%BA%A9n-%C4%91o%C3%A1n-dpl",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-emergency-medicine-procedures/how-to-do-diagnostic-peritoneal-lavage-dpl",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E7%B7%8A%E6%80%A5%E5%8C%BB%E7%99%82%E5%87%A6%E7%BD%AE/%E8%A8%BA%E6%96%AD%E7%9A%84%E8%85%B9%E8%85%94%E6%B4%97%E6%B5%84%EF%BC%88dpl%EF%BC%89"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-c%E1%BA%A5p-c%E1%BB%A9u-kh%C3%A1c-trong-y-khoa/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-ki%E1%BB%83m-tra-e-fast",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-emergency-medicine-procedures/how-to-do-e-fast-examination",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E7%B7%8A%E6%80%A5%E5%8C%BB%E7%99%82%E5%87%A6%E7%BD%AE/e-fast%E3%81%AB%E3%82%88%E3%82%8B%E8%A8%BA%E5%AF%9F"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/c%C3%A1ch-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A1c-th%E1%BB%A7-thu%E1%BA%ADt-c%E1%BA%A5p-c%E1%BB%A9u-kh%C3%A1c-trong-y-khoa/c%C3%A1ch-si%C3%AAu-%C3%A2m",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/how-to-do-other-emergency-medicine-procedures/how-to-do-ultrasonography",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E7%B7%8A%E6%80%A5%E5%8C%BB%E7%99%82%E5%87%A6%E7%BD%AE/%E8%B6%85%E9%9F%B3%E6%B3%A2%E6%A4%9C%E6%9F%BB"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-th%E1%BB%9F/t%E1%BB%95ng-quan-v%E1%BB%81-ng%E1%BB%ABng-th%E1%BB%9F",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-arrest/overview-of-respiratory-arrest",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E5%81%9C%E6%AD%A2/%E5%91%BC%E5%90%B8%E5%81%9C%E6%AD%A2%E3%81%AE%E6%A6%82%E8%A6%81"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-th%E1%BB%9F/thi%E1%BA%BFt-l%E1%BA%ADp-v%C3%A0-ki%E1%BB%83m-so%C3%A1t-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-arrest/airway-establishment-and-control",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E5%81%9C%E6%AD%A2/%E6%B0%97%E9%81%93%E7%A2%BA%E4%BF%9D%E3%81%8A%E3%82%88%E3%81%B3%E7%AE%A1%E7%90%86"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-th%E1%BB%9F/thi%E1%BA%BFt-b%E1%BB%8B-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F-v%C3%A0-th%C3%B4ng-kh%C3%AD",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-arrest/airway-and-respiratory-devices",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E5%81%9C%E6%AD%A2/%E6%B0%97%E9%81%93%E7%A2%BA%E4%BF%9D%E3%81%8A%E3%82%88%E3%81%B3%E4%BA%BA%E5%B7%A5%E5%91%BC%E5%90%B8%E3%81%AE%E5%99%A8%E5%85%B7"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-th%E1%BB%9F/%C4%91%E1%BA%B7t-n%E1%BB%99i-kh%C3%AD-qu%E1%BA%A3n",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-arrest/tracheal-intubation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E5%81%9C%E6%AD%A2/%E6%B0%97%E7%AE%A1%E6%8C%BF%E7%AE%A1"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-th%E1%BB%9F/ph%E1%BA%ABu-thu%E1%BA%ADt-%C4%91%C6%B0%E1%BB%9Dng-th%E1%BB%9F",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-arrest/surgical-airway",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E5%81%9C%E6%AD%A2/%E5%A4%96%E7%A7%91%E7%9A%84%E6%B0%97%E9%81%93%E7%A2%BA%E4%BF%9D"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/ng%E1%BB%ABng-th%E1%BB%9F/thu%E1%BB%91c-%C4%91%E1%BB%83-h%E1%BB%97-tr%E1%BB%A3-%C4%91%E1%BA%B7t-n%E1%BB%99i-kh%C3%AD-qu%E1%BA%A3n",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-arrest/drugs-to-aid-intubation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E5%81%9C%E6%AD%A2/%E6%8C%BF%E7%AE%A1%E3%82%92%E8%A3%9C%E5%8A%A9%E3%81%99%E3%82%8B%E8%96%AC%E5%89%A4"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/suy-h%C3%B4-h%E1%BA%A5p-v%C3%A0-th%C3%B4ng-kh%C3%AD-c%C6%A1-h%E1%BB%8Dc/t%E1%BB%95ng-quan-v%E1%BB%81-suy-h%C3%B4-h%E1%BA%A5p",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-failure-and-mechanical-ventilation/overview-of-respiratory-failure",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8%E3%81%8A%E3%82%88%E3%81%B3%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97/%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8%E3%81%AE%E6%A6%82%E8%A6%81"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/suy-h%C3%B4-h%E1%BA%A5p-v%C3%A0-th%C3%B4ng-kh%C3%AD-c%C6%A1-h%E1%BB%8Dc/t%E1%BB%95ng-quan-v%E1%BB%81-th%C3%B4ng-kh%C3%AD-c%C6%A1-h%E1%BB%8Dc",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-failure-and-mechanical-ventilation/overview-of-mechanical-ventilation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8%E3%81%8A%E3%82%88%E3%81%B3%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97/%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97%E3%81%AE%E6%A6%82%E8%A6%81"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/suy-h%C3%B4-h%E1%BA%A5p-v%C3%A0-th%C3%B4ng-kh%C3%AD-c%C6%A1-h%E1%BB%8Dc/suy-h%C3%B4-h%E1%BA%A5p-c%E1%BA%A5p-gi%E1%BA%A3m-oxy-ahrf,-ards",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-failure-and-mechanical-ventilation/acute-hypoxemic-respiratory-failure-ahrf,-ards",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8%E3%81%8A%E3%82%88%E3%81%B3%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97/%E6%80%A5%E6%80%A7%E4%BD%8E%E9%85%B8%E7%B4%A0%E8%A1%80%E7%97%87%E6%80%A7%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8-%EF%BC%88ahrf%EF%BC%8Cards%EF%BC%89"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/suy-h%C3%B4-h%E1%BA%A5p-v%C3%A0-th%C3%B4ng-kh%C3%AD-c%C6%A1-h%E1%BB%8Dc/th%C3%B4ng-kh%C3%AD-th%E1%BA%A5t-b%E1%BA%A1i",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-failure-and-mechanical-ventilation/ventilatory-failure",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8%E3%81%8A%E3%82%88%E3%81%B3%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97/%E6%8F%9B%E6%B0%97%E4%B8%8D%E5%85%A8"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/suy-h%C3%B4-h%E1%BA%A5p-v%C3%A0-th%C3%B4ng-kh%C3%AD-c%C6%A1-h%E1%BB%8Dc/c%C3%A1c-lo%E1%BA%A1i-suy-h%C3%B4-h%E1%BA%A5p-kh%C3%A1c",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-failure-and-mechanical-ventilation/other-types-of-respiratory-failure",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8%E3%81%8A%E3%82%88%E3%81%B3%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E7%A8%AE%E9%A1%9E%E3%81%AE%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/suy-h%C3%B4-h%E1%BA%A5p-v%C3%A0-th%C3%B4ng-kh%C3%AD-c%C6%A1-h%E1%BB%8Dc/cai-m%C3%A1y-th%E1%BB%9F",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/respiratory-failure-and-mechanical-ventilation/liberation-from-mechanical-ventilation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E5%91%BC%E5%90%B8%E4%B8%8D%E5%85%A8%E3%81%8A%E3%82%88%E3%81%B3%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97/%E6%A9%9F%E6%A2%B0%E7%9A%84%E4%BA%BA%E5%B7%A5%E6%8F%9B%E6%B0%97%E3%81%8B%E3%82%89%E3%81%AE%E9%9B%A2%E8%84%B1"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/nhi%E1%BB%85m-khu%E1%BA%A9n-huy%E1%BA%BFt-v%C3%A0-s%E1%BB%91c-nhi%E1%BB%85m-khu%E1%BA%A9n/nhi%E1%BB%85m-khu%E1%BA%A9n-huy%E1%BA%BFt-v%C3%A0-s%E1%BB%91c-nhi%E1%BB%85m-khu%E1%BA%A9n",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/sepsis-and-septic-shock/sepsis-and-septic-shock",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E6%95%97%E8%A1%80%E7%97%87%E3%81%8A%E3%82%88%E3%81%B3%E6%95%97%E8%A1%80%E7%97%87%E6%80%A7%E3%82%B7%E3%83%A7%E3%83%83%E3%82%AF/%E6%95%97%E8%A1%80%E7%97%87%E3%81%8A%E3%82%88%E3%81%B3%E6%95%97%E8%A1%80%E7%97%87%E6%80%A7%E3%82%B7%E3%83%A7%E3%83%83%E3%82%AF"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/s%E1%BB%91c-v%C3%A0-h%E1%BB%93i-s%E1%BB%A9c-d%E1%BB%8Bch/s%E1%BB%91c",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/shock-and-fluid-resuscitation/shock",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%82%B7%E3%83%A7%E3%83%83%E3%82%AF%E3%81%8A%E3%82%88%E3%81%B3%E8%BC%B8%E6%B6%B2%E8%98%87%E7%94%9F/%E3%82%B7%E3%83%A7%E3%83%83%E3%82%AF"
    },
    {
        "vi": "https://www.msdmanuals.com/vi-vn/chuy%C3%AAn-gia/y-h%E1%BB%8Dc-ch%C4%83m-s%C3%B3c-tr%E1%BB%8Dng-t%C3%A2m/s%E1%BB%91c-v%C3%A0-h%E1%BB%93i-s%E1%BB%A9c-d%E1%BB%8Bch/h%E1%BB%93i-s%E1%BB%A9c-t%C4%A9nh-m%E1%BA%A1ch",
        "en": "https://www.msdmanuals.com/professional/critical-care-medicine/shock-and-fluid-resuscitation/intravenous-fluid-resuscitation",
        "ja": "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/21-%E6%95%91%E5%91%BD%E5%8C%BB%E7%99%82/%E3%82%B7%E3%83%A7%E3%83%83%E3%82%AF%E3%81%8A%E3%82%88%E3%81%B3%E8%BC%B8%E6%B6%B2%E8%98%87%E7%94%9F/%E8%BC%B8%E6%B6%B2%E8%98%87%E7%94%9F%EF%BC%88fluid-resuscitation%EF%BC%89"
    }
]
