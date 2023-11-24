(function cralwer() {
    const urls = Array.from(document.querySelectorAll(".sidebar__sticky .box__content--container .box__content .othertopics__listings a")).map(x => x.href)
    if (location.href.includes("/vi")) {
        console.log({vi: urls});
        return;
    } else if (location.href.includes("/ja-jp")) {
        console.log({ja: urls});
    } else {
        console.log({en: urls});
    }
})()
