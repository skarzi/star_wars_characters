import { MutationTree } from 'vuex'
import { CharactersStateInterface } from './state'
import { RawCharacter } from './interfaces'
import { processCharacter } from './utils'
import { CollectionMeta } from '../../components/models'

const mutation: MutationTree<CharactersStateInterface> = {
  processCharacters (
    state: CharactersStateInterface,
    rawCharacters: Array<RawCharacter>
  ) {
    const characters = rawCharacters.map(processCharacter)
    state.characters = [...state.characters, ...characters]
  },
  setTotalCount (state: CharactersStateInterface, newTotalCount: number) {
    state.totalCount = newTotalCount
  },
  setNextPage (state: CharactersStateInterface, newNextPage: string) {
    state.nextPage = newNextPage
  },
  setMeta (state: CharactersStateInterface, newMeta: CollectionMeta) {
    state.meta = newMeta
  },
  clearCharactersData (state: CharactersStateInterface) {
    state.characters = []
    state.totalCount = 0
    state.nextPage = ''
    state.meta = null
  }
}

export default mutation
