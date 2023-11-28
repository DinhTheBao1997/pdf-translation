(function crawlerLink() {
    const els = document.querySelectorAll(".medicalsection.main__content>.medicalsection__main>ul>li>div.medicalsection__column>ul>li>a");
    const links = Array.from(els).map(el => el.href);
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
