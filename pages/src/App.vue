<!-- App.vue -->

<template>
  <!-- App.vue -->

  <v-app>
    <v-app-bar color="red" app>
      <v-toolbar-title>Title</v-toolbar-title>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-content>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
        <!-- each row contains 12 columns -->
        <v-row>
          <v-col cols="2"> </v-col>
          <v-col cols="8">
            <div id="content"><p>Place Notes Here</p></div>
          </v-col>
          <v-col cools="2"> </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer color="red" app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

