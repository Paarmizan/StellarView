<template>

  <v-app>
    <router-view/>
    <card-d-i/>
  </v-app>
</template>

<script>

import CardDI from "@/components/CardDataInput.vue";

export default {
  name: 'App',

  components: {
    CardDI
  },

  data: () => ({
    //
  }),
};
</script>

<style>
#app{
  background-color: black;
}
</style>


