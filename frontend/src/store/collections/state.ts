import { Collection } from '../../components/models'

export interface CollectionsStateInterface {
  collections: Array<Collection>
  nextPage: string
  totalCount: number
}

const state: CollectionsStateInterface = {
  collections: [],
  nextPage: '',
  totalCount: 0
}

export default state
