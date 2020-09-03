export interface RawCharacter {
  url: string;
  name: string;
  height: string;
  /* eslint-disable camelcase */
  hair_color: string;
  eye_color: string;
  birth_year: string;
  /* eslint-enable camelcase */
  gender: string;
  homeworld: string;
  date: string;
}

export interface CharactersResponse {
  data: Array<RawCharacter>
  count: number
  next: string
  previous: string
}

export interface AxiosCharactersResponse {
  data: CharactersResponse
  status: number
}
