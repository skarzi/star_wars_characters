import { CollectionMeta, Character } from '../../components/models'

export interface CharactersStateInterface {
  characters: Array<Character>
  filename: string
  nextPage: string
  totalCount: number
  meta: CollectionMeta | null
}

const state: CharactersStateInterface = {
  meta: null,
  characters: [],
  filename: '',
  nextPage: '',
  totalCount: 0
}

export default state
