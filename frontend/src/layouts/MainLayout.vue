<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-black">
      <q-toolbar>
        <q-toolbar-title class="text-warning text-center">
          Star Wars Characters
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
export default class MainLayout extends Vue {
  created () {
    this.$q.dark.set(true)
  }
}
</script>
