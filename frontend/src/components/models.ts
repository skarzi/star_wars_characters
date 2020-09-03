export interface Collection {
  id: number;
  createdAt: Date;
}

export interface Character {
  url: string;
  name: string;
  height: string;
  hairColor: string;
  eyeColor: string;
  birthYear: string;
  gender: string;
  homeworld: string;
  date: string;
}

export interface FieldCount {
  [name: string]: string | number;
  count: number;
}

export interface CollectionMeta {
  file: string;
  filename: string;
  createdAt: Date;
}
