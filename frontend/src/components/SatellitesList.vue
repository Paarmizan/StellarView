<template>
  <div class="satellites-list" ref="satellitesList">
    <h2 class="clr_blue satellites-list__title">Список спутников</h2>
    <table style="width: 100%; border-collapse: collapse">
    <thead class="thead-satellite">
      <tr style="width: 100%;">
        <th class="td-satellite">Спутник</th>
        <th class="td-satellite">Координаты</th>
        <th class="td-satellite">Запросы</th>
        <th class="td-satellite">Доступность</th>
      </tr>
    </thead>
    <tbody style="width: 100%;">
      <tr v-for="data in dt" :key="data.satellite">
        <td class="td-satellite">{{ data.satellite }}</td>
        <td class="td-satellite">{{ data.cords }}</td>
        <td class="td-satellite">{{ data.requests }}</td>
        <td class="td-satellite clr_blue">{{ data.availability }}</td>
      </tr>
    </tbody>
  </table>
  </div>
</template>

<script>
export default {
  name: 'satellitesList',

  props: {
  },

  data() {
    return {
      itemsPerPage: 5,

      headers: [
          { title: 'Спутник', align: 'end', key: 'satellite' },
          { title: 'Координаты', align: 'end', key: 'cords' },
          { title: 'Запросы', align: 'end', key: 'requests' },
          { title: 'Доступность', align: 'end', key: 'availability' },
      ],

      dt: [
          {
            satellite: 'Спутник1',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник2',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник3',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник4',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник5',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник6',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник6',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник6',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
          {
            satellite: 'Спутник6',
            cords: '21’N 40’E ',
            requests: '340 запросов',
            availability: 'Доступен',
          },
      ],
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

.satellites-list {
  background-color: white;
}

.td-satellite {
  width: 25%;
  text-align: center;
  font-size: 20px;
  padding: 10px 0;
}

.thead-satellite .td-satellite {
  font-size: 30px;
}

.thead-satellite {
    position: relative;
}

.thead-satellite::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 2%;
  width: 96%;
  border-bottom: 2px solid black;
}

.clr_blue {
  color: #15C6E9;
}

.satellites-list__title {
  font-weight: 400;
  margin-left: 125px;
  position: relative;
}
</style>