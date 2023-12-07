/**
 * This project is mantainer for teams
 * Carlos bonet
 * Gerzon Rangel
 * Sebastian Garcia
 * Santiago Rico
 * Deno
 * Mit License @copyright 2023
 */

import { example } from 'deps/const.ts';

console.log(example);

const start = () => {
  Deno.serve(() => new Response('Hello World'));
};

export default start;
