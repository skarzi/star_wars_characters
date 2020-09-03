import { Character } from '../../components/models'

export interface CharactersStateInterface {
  characters: Array<Character>
  filename: string
  nextPage: string
  totalCount: number
}

const state: CharactersStateInterface = {
  characters: [],
  filename: '',
  nextPage: '',
  totalCount: 0
}

export default state
