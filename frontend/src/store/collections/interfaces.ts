export interface RawCollection {
  id: number
  created_at: string // eslint-disable-line camelcase
}

export interface RawResponseData {
  collections: Array<RawCollection>
}

export interface PeopleCollectionResponse {
  data: Array<RawCollection>
  count: number
  next: string
  previous: string
}

export interface AxiosPeopleCollectionResponse {
  data: PeopleCollectionResponse
  status: number
}

export interface CreatePeopleCollectionResponse {
  data: RawCollection
  count: number
  next: string
  previous: string
}

export interface AxiosCreatePeopleCollectionResponse {
  data: CreatePeopleCollectionResponse
  status: number
}
