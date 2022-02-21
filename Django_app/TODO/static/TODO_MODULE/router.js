"use strict";
//インポート
import { GENRE } from "./GENRE.js";
import { GOAL } from "./GOAL.js";
import { TODO_HEADER } from "./TODO_HEADER.js";
import { TODO_DETAIL } from "./TODO_DETAIL.js";
import { MEMO } from "./MEMO.js";
import { TODO_MANAGE } from "./TODO_MANAGE.js";
//ルータ
const router = new VueRouter({
    routes: [
        GENRE,
        GOAL,
        TODO_HEADER,
        TODO_DETAIL,
        MEMO,
        TODO_MANAGE,
    ]
});
export { router };