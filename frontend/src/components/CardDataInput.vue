<template>
  <div class="card">
    <div class="N">
      <div class="vraper">
        <v-col>
        <v-text-field
            class="input"
            label="`N"
            placeholder="xx"
        ></v-text-field>
      </v-col>
      </div>
    </div>
    <div class="E">
      <div class="vraper">
        <v-col>
          <v-text-field
              class="input"
              label="`E"
              placeholder="xx"
          ></v-text-field>
        </v-col>
      </div>
    </div>
    <div class="vraper_2">
      <v-text-field
          label="Введите адресс"
          placeholder="johndoe@gmail.com"
          type="email"
      ></v-text-field>
    </div>
    <div class="vraper_3">
      <v-autocomplete
        chips
        label="Выберете разрешение"
        :items="['4:3', '16:9', '16:10']"
      ></v-autocomplete>
    </div>
    <div>
      <btn-s-s>
        Искать спутник по параметрам
      </btn-s-s>
    </div>
    <div class="CardPrice">
      <div class="OutputPrice">
        <p>Цена: n/a руб.</p>
      </div>
    </div>



  </div>
</template>

<script>
import BtnSS from "@/components/ButtinSearchSatellites.vue";

export default {
  name:"cardDI",
  components: {BtnSS}

}
</script>

<style lang="scss" scoped>
.card{
  width: 562px;
  height: 569px;
  flex-shrink: 0;
  border-radius: 19px;
  background: rgba(255, 255, 255, 0.30);
}
.vraper{
  border-radius: 10px;
  background: #DBD6D6;
  width: 240px;
  height: 65px;
  color: black;
  text-align: center;
  font-size: 32px;

}
.N{
  position: absolute;
  margin-top: 26px;
  margin-left: 32px;
}
.E{
  position: absolute;
  margin-top: 26px;
  margin-left: 289px;
}
.vraper_2{
  position: absolute;
  margin-top: 111px;
  margin-left: 32px;
  width: 497px;
  height: 65px;
  border-radius: 10px;
  background: #DBD6D6;
  color: black;
  text-align: center;
  font-size: 34px;
  padding: 10px;
}
.vraper_3{
  position: absolute;
  margin-top: 196px;
  margin-left: 32px;
  width: 497px;
  height: 65px;
  border-radius: 10px;
  background: #DBD6D6;
  color: black;
  text-align: center;
  font-size: 34px;
  padding: 10px;
}
.CardPrice{
  position: absolute;
  margin-top: 501px;
  margin-left: 32px;
}
.OutputPrice{
  border-radius: 10px;
  background: #DBD6D6;
  width: 251px;
  height: 41px;
  color: black;
  text-align: center;
  font-size: 28px;
}


</style>