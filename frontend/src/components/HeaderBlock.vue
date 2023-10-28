<template>
  <div class="header-block" ref="headerBlock">
   <v-app-bar class="header-block__bar">
     <v-spacer/>
     <div class="d-flex align-center">
       <h1 class="header-block__title">Stellar View</h1>
       <div class="header-block__logo"><img src="@/assets/logo.svg" alt="logo"></div>
     </div>
     <v-spacer/>
     <v-spacer/>
     <v-spacer/>
     <v-spacer/>
     <v-spacer/>
     <div style="width: 300px">
       <v-text-field
         outlined
         class="header-block__search"
         placeholder="Поиск"
         hide-details
         style="width: 100%"
     >
     </v-text-field>
     </div>
     <v-spacer/>
   </v-app-bar>
  </div>
</template>

<script>
import HeaderBlock from "@/components/HeaderBlock.vue";
export default {
  name: 'HeaderBlock',

  comments: {HeaderBlock},

  props: {
  },

  data() {
    return {
    }
  },

  computed: {
  },

  created() {
  },

  methods: {
  },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;700&display=swap');

.header-block {
  position: fixed;
  width: 100%;
  padding: 0 40px;
}

.header-block__bar{
  border-bottom: 3px solid white;
  background-color: transparent!important;
  height: 80px!important;
  width: 100%;
  padding-top: 10px;
}

.header-block__title {
  font-family: 'Noto Sans', sans-serif;
  color: white;
}

.header-block__logo {
  margin-left: 20px;
}

.header-block__search {
  border: 3px solid white;
  border-radius: 30px;
  color: white;
  width: 1px;
}

.header-block__search input{
  color: white!important;
}

.header-block__search:hover {
  border: 4px solid white;
  border-radius: 30px;
}

.header-block__search:focus {
  border: 5px solid white;
  border-radius: 30px;
}
</style>