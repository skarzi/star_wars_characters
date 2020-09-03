import { MutationTree } from 'vuex'
import { CharactersStateInterface } from './state'
import { RawCharacter } from './interfaces'
import { processCharacter } from './utils'

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
  clearCharactersData (state: CharactersStateInterface) {
    state.characters = []
    state.totalCount = 0
    state.nextPage = ''
  }
}

export default mutation
