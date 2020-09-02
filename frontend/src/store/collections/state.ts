import { Collection } from '../../components/models'

export interface CollectionsStateInterface {
  wasRequestSent: boolean
  collections: Array<Collection>
  nextPage: string
  totalCount: number
}

const state: CollectionsStateInterface = {
  wasRequestSent: false,
  collections: [],
  nextPage: '',
  totalCount: 0
}

export default state
