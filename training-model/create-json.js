(function createJSON() {
    const objs = [
        {
            "ja": [
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E5%A4%96%E6%9D%A5ph%E3%83%A2%E3%83%8B%E3%82%BF%E3%83%AA%E3%83%B3%E3%82%B0",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E8%82%9B%E9%96%80%E9%8F%A1%E6%A4%9C%E6%9F%BB%E3%81%A8s%E7%8A%B6%E7%B5%90%E8%85%B8%E9%8F%A1%E6%A4%9C%E6%9F%BB",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E5%86%85%E8%A6%96%E9%8F%A1%E6%A4%9C%E6%9F%BB",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E8%83%83%E6%B6%B2%E6%A4%9C%E6%9F%BB",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E8%85%B9%E8%85%94%E9%8F%A1%E6%A4%9C%E6%9F%BB",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E5%86%85%E5%9C%A7%E6%A4%9C%E6%9F%BB",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E7%B5%8C%E9%BC%BB%E8%83%83%E7%AE%A1%E3%81%BE%E3%81%9F%E3%81%AF%E3%82%A4%E3%83%AC%E3%82%A6%E3%82%B9%E7%AE%A1%E6%8C%BF%E5%85%A5",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E6%A0%B8%E5%8C%BB%E5%AD%A6%E6%B6%88%E5%8C%96%E7%AE%A1%E6%A4%9C%E6%9F%BB",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E7%A9%BF%E5%88%BA",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AEx%E7%B7%9A%E3%81%8A%E3%82%88%E3%81%B3%E4%BB%96%E3%81%AE%E9%80%A0%E5%BD%B1%E6%A4%9C%E6%9F%BB",
                "https://www.msdmanuals.com/ja-jp/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB/01-%E6%B6%88%E5%8C%96%E7%AE%A1%E7%96%BE%E6%82%A3/%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E8%A8%BA%E6%96%AD%E3%81%A8%E6%B2%BB%E7%99%82%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%89%8B%E6%8A%80/%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E6%B6%88%E5%8C%96%E7%AE%A1%E3%81%AE%E6%A4%9C%E6%9F%BB%E6%96%B9%E6%B3%95"
            ]
        }
    ]
    const results = {};
    for (const obj of objs) {
        for (const [lang, lst] of Object.entries(obj)) {
            results[lang] = lst;
        }
    }
    console.log(results)
})()