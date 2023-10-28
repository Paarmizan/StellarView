<template>
  <div class="tariff-card" ref="tariffCars">
    <div class="tariff-card__img"><img src="@/assets/Vector.png"></div>
    <div class="tariff-card__title">{{ title }}</div>
    <div class="tariff-card__text">{{ text }}</div>
    <div class="tariff-card__price">{{ price }}</div>
  </div>
</template>

<script>
export default {
  name: 'tariffCars',

  props: {
    title: {type: String},
    text: {type: String},
    price: {type: String},
  },

  data() {
    return {
    }
  },

  computed: {
  },

  created() {
  },

  mounted() {
  },

  methods: {
  },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;700&display=swap');

.tariff-card {
  background-color: white;
  border: 1px solid red;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.tariff-card__img {
  position: relative;
  margin-bottom: 10px;
}

.tariff-card__title {
  font-size: 24px;
  position: relative;
  width: 100%;
  text-align: center;
  margin-bottom: 20px;
}

.tariff-card__title::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 10%;
  width: 80%;
  border-bottom: 2px solid black;
}

.tariff-card__text {
  position: relative;
  width: 80%;
}

.tariff-card__text::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 10%;
  width: 80%;
  border-bottom: 2px solid black;
}
</style>