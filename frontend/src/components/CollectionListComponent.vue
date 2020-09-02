<template>
  <q-list dark bordered separator>
    <q-item
      v-for="collection in collections"
      :key="collection.id"
      :to="{ name: 'collection-detail', params: { id: collection.id } }"
    >
      <q-item-label>
        {{ collection.createdAt.toLocaleString() }}
      </q-item-label>
    </q-item>
  </q-list>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Collection } from './models'

@Component
export default class CollectionList extends Vue {
  @Prop({ type: Array, default: () => [] }) readonly collections!: Collection[]
}
</script>
