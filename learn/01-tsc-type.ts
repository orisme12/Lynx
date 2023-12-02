const tags_dev: string = 'Tags Dev';

const tags_number: number = 10;

const tags_boolean: boolean = true;

const tags_null: null = null;

const tags_array: Array<string> = ['', ''];

const tags_array_version2: string[] = [];

let two_types_string_number: string | number = 10;

let array_two_type: (string | number)[] = [10, '10'];

two_types_string_number = '10';

let type_any: any = 10;

type_any = '10';
type_any = null;
type_any = [];

let type_unknow: unknown = 10;

type_unknow = '10';

console.log({
  tags_dev,
  tags_number,
  tags_boolean,
  tags_null,
  tags_array,
  tags_array_version2,
  two_types_string_number,
  array_two_type,
});
