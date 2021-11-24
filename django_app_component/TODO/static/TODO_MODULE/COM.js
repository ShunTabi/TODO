"use strict";
const COM_highlight = (tg, val) => {
    const result = tg.replace(val, `<font class="span_highlight">${val}</font>`);
    console.log(result);
    return result;
}

export { COM_highlight, }