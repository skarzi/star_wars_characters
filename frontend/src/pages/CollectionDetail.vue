<template>
  <q-page class="row items-start justify-evenly q-py-md">
    <q-table
      row-key="name"
      :data="characters"
      :columns="columns"
      :loading="isLoading"
      :pagination.sync="pagination"
      color="primary"
      card-class="bg-black text-primary"
      flat
      square
    >
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
            class="text-weight-bold text-uppercase"
          >
            <q-checkbox
              v-model="selectedFieldNames"
              :val="col.name"
              :label="col.label"
              dense
            />
          </q-th>
        </q-tr>
      </template>

      <template v-slot:top>
        <a :href="meta.file">
          {{ meta.filename }}
        </a>
        <q-space />
        <q-btn
          color="primary"
          :disable="selectedFieldNames.length == 0"
          label="Count Field Values"
          :to="{name: 'collections-fields-counts', params: {id: $route.params.id, fieldNames: selectedFieldNames.join(',')}}"
        />
      </template>

      <template v-slot:bottom>
        <q-space />
        <div class="q-pa-md">
          <q-btn
            @click="loadMoreCharacters"
            label="Load more"
            icon="cloud_download"
            :disabled="!nextPage"
          />
        </div>
        <q-space />
      </template>
    </q-table>
  </q-page>
</template>

<script lang="ts">
import { Character, CollectionMeta } from 'components/models'
import { Vue, Component } from 'vue-property-decorator'
import { createNamespacedHelpers } from 'vuex'

const charactersNamespace = createNamespacedHelpers('characters')

@Component({
  computed: charactersNamespace.mapState([
    'characters',
    'totalCount',
    'nextPage',
    'meta'
  ]),
  methods: charactersNamespace.mapActions([
    'fetchCharacters',
    'clearCharactersData'
  ])
})
export default class CollectionDetail extends Vue {
  // state
  characters!: Character[]
  totalCount!: number
  nextPage!: string
  nextPage!: CollectionMeta
  // actions
  fetchCharacters!: () => Promise<void>
  clearCharactersData!: () => void

  isLoading = false

  columns = [
    { name: 'name', field: 'name', label: 'Name' },
    { name: 'height', field: 'height', label: 'Height' },
    { name: 'hair_color', field: 'hairColor', label: 'Hair Color' },
    { name: 'eye_color', field: 'eyeColor', label: 'Eye Color' },
    { name: 'birth_year', field: 'birthYear', label: 'Birth Year' },
    { name: 'gender', field: 'gender', label: 'Gender' },
    { name: 'homeworld', field: 'homeworld', label: 'Homeworld' },
    { name: 'date', field: 'date', label: 'Date' }
  ]

  pagination = {
    page: 1,
    rowsPerPage: 10,
    rowsNumber: 0
  }

  selectedFieldNames: Array<string> = []

  async created () {
    this.clearCharactersData()
    await this.fetchCharacters(`collections/people/${this.$route.params.id}`)
  }

  async loadMoreCharacters () {
    if (this.nextPage) {
      this.isLoading = true
      await this.fetchCharacters(this.nextPage)
      this.pagination.rowsPerPage += 10
      this.pagination.rowsNumber = this.totalCount
      this.isLoading = false
    }
  }
}
</script>
