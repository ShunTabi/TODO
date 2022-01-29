"use strict";
//インポート
import { GENRE_ } from "./GENRE.js";
import { GOAL_ } from "./GOAL.js";
import { TODO_HEADER_ } from "./TODO_HEADER.js";
import { TODO_DETAIL_ } from "./TODO_DETAIL.js";
import { MEMO_ } from "./MEMO.js";
//ルータ
const router = new VueRouter({
    routes: [
        GENRE_,
        GOAL_,
        TODO_HEADER_,
        TODO_DETAIL_,
        MEMO_,
    ]
});
export { router };