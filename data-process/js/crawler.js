(function crawlerLink() {
    const topics = ".section__list--2col a";
    const details = ".medicalsection.main__content>.medicalsection__main>ul>li>div.medicalsection__column>ul>li>a";
    const langs = "#ui-id-2 option"
    const query=langs;
    // const els = document.querySelectorAll();
    const els = document.querySelectorAll(query);
    // const links = Array.from(els).map(el => el.href); // topics, details
    const links = Array.from(els).map(el => el.value); // langs
    console.log(links)
})()

(function getText() {
    /**
     * 
     * @param {string} v 
     * @returns 
     */
    const isIgnore = (v) => {
        if (!v) return true;
        return !!v.match(/^[\d]+\./);
    }
    const queries = [
        "div.topic__accordion>div.para>p",
        "div.topic__accordion> section div.topic__content div.list .topic__listitem",
        "div.topic__accordion> section div.topic__content>div.para>p"
    ];
    const text = []
    const func = (query) => {
        const els = document.querySelectorAll(query);
        els.forEach(el => {
            const v = el.textContent.trim();
            if (isIgnore(v)) return;
            text.push(v);
        })
    }
    queries.forEach(query=>func(query));
    console.log(text)
})()
