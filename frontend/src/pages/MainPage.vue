<template>
  <div class="main-page d-flex flex-column" ref="MainPage" >
    <HeaderBlock/>
    <div
        class="main-page__block main-page__block1"
    >
      <div style="height: 50%; position: relative">
        <div class="main-page__block1-text">Привет! Мы - StellarView - компания, которая занимается<br>оптимизацией и предоставлением актуальной информации <br>о данных земли, с помощью спутниковой съемки. Ниже вы <br>можете заказать наши услуги.</div>
      </div>
      <div style="height: 50%">

      </div>
    </div>

    <div
        class="main-page__block main-page__block2"
    >
    </div>

    <div
        class="main-page__block main-page__block3"
    >
    </div>

    <div
        class="main-page__block main-page__block4"
    >
    </div>
  </div>
</template>

<script>
import HeaderBlock from "@/components/HeaderBlock.vue";
export default {
  name: 'MainPage',

  components: {HeaderBlock},

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

.main-page {
  background: url("../assets/bg.jpg") 0 0 / cover repeat-y;
  min-height: 100vh;
}

.main-page__block {
    height: 100vh;
}

.main-page__block1 {
  background: url("../assets/cb.png") -30px 60px / contain no-repeat;
  position: relative;
}

.main-page__block1-text {
  font-family: 'Noto Sans', sans-serif;
  background: #D9D9D9;
  font-size: 22px;
  width: 730px;
  border-radius: 150px;
  text-align: center;
  padding: 10px 20px;
  position: absolute;
  right: 220px;
  bottom: 80px;
}

</style>