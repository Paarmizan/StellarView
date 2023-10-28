<template>
  <v-card :loading="loading" class="shade-w mx-auto my-12" width="262px" height="489px">
    <template v-slot:loader="{ isActive }">
      <v-progress-linear
        :active="isActive"
        color="deep-purple"
        height="4"
        indeterminate
      ></v-progress-linear>
    </template>
    <div class="img-car">
      <v-img
          cover
          width="100%"
          src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
          viewBox="0 0 177 155"
          fill="none"
      ></v-img>
    </div>

    <v-card-title>Cafe Badilico</v-card-title>

    <v-divider class="mx-4 mb-1"></v-divider>

    <v-card-text>
      <div>
        Small plates, salads & sandwiches - an intimate setting with 12 indoor
        seats plus patio seating.
      </div>
    </v-card-text>

    <v-divider class="mx-4 mb-1"></v-divider>

    <v-card-title class="titleCard">Tonight's availability</v-card-title>

  </v-card>
</template>

<script>
  export default {

  }

</script>

<style>
.titleCard{
  text-align: center;
}

.img-car{
  background-size:  cover;


}


.shade-w {
    position: relative;
  z-index: 2;

  &:after {
    content: "";
    position: absolute;
    width: 110%;
    height: 110%;
    left: -5%;
    top: -5%;
    background: #fff;
    opacity: 40%;
    z-index: -1;
  }
}
</style>