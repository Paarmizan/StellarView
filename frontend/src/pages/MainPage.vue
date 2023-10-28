<template>
  <div class="main-page d-flex flex-column" ref="MainPage" >
    <HeaderBlock/>
    <div
        class="main-page__block main-page__block1"
    >
      <div style="height: 50%; position: relative">
        <div class="main-page__block1-text">Привет! Мы - StellarView - компания, которая занимается<br>оптимизацией и предоставлением актуальной информации <br>о данных земли, с помощью спутниковой съемки. Ниже вы <br>можете заказать наши услуги.</div>
      </div>
      <div style="height: 50%; padding: 0 30px" class="d-flex flex-column align-end justify-md-space-around">
        <ButtonOrder>Заказать</ButtonOrder>
        <ButtonTariffsSatellites>Тарифы</ButtonTariffsSatellites>
        <ButtonTariffsSatellites>Спутники</ButtonTariffsSatellites>
      </div>
    </div>

    <div
        class="main-page__block main-page__block2 block2"
    >
      <h2 class="block2__title">Тарифы</h2>
      <div class="block2__cards d-flex justify-space-around">
        <TariffCard
            :title="'Базовый'"
            :text="'Действует для спутников с расчетным временем более 5 дней'"
            :price="'~ 800 руб'"
            class="tariff-card"
            ></TariffCard>
        <TariffCard
            :title="'Основной'"
            :text="'Действует для спутников с расчетным временем от 2 до 3 дней'"
            :price="'~ 1500 руб'"
            class="tariff-card"
        ></TariffCard>
        <TariffCard
            :title="'Продвинутый'"
            :text="'Действует для спутников с расчетным временем менее 3 дней'"
            :price="'~ 2000 руб'"
            class="tariff-card"
        ></TariffCard>
      </div>
    </div>

    <div
        class="main-page__block main-page__block3"
    >
    </div>

    <div
        class="main-page__block main-page__block4"
    >
      <SatellitesList></SatellitesList>
    </div>
  </div>
</template>

<script>
import HeaderBlock from "@/components/HeaderBlock.vue";
import ButtonOrder from "@/components/ButtonOrder.vue";
import ButtonTariffsSatellites from "@/components/ButtonTariffsSatellites.vue";
import TariffCard from "@/components/TariffCard.vue";
import SatellitesList from "@/components/SatellitesList.vue";
export default {
  name: 'MainPage',

  components: {HeaderBlock, ButtonOrder, ButtonTariffsSatellites, TariffCard, SatellitesList},

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
}

.main-page__block {
  height: 100vh;
  padding: 100px 12px 0 12px;
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
  bottom: 120px;
}

.main-page__block2 {
  padding-top: 180px;
}

.block2__title {
  width: 80%;
  margin: 0 auto 60px auto;
  text-align: center;
  vertical-align: middle;
  height: 60px;
  background: white;
  border-radius: 19px;
  font-size: 36px;
}

.tariff-card {
  width: 20%;
}

.main-page__block4 {
  padding-top: 130px;
}
</style>